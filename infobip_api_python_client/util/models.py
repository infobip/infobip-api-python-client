from datetime import datetime
import json

__author__ = 'mstipanov'


class DateFormatIso8601(object):
    @classmethod
    def strftime(cls, d):
        s = "%04d-%02d-%02dT%02d:%02d:%02d.%03d" % (
            d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond / 1000)

        tzinfo = d.tzinfo
        if not tzinfo:
            return s

        offset_seconds = tzinfo._offset.seconds
        if (offset_seconds < 0):
            s = s + "-"
        else:
            s = s + "+"

        m, sec = divmod(abs(offset_seconds), 60)
        h, m = divmod(m, 60)

        s = s + "%02d%02d" % (int(h), int(m))
        return s

    @classmethod
    def strptime(cls, line):
        year = int(line[0:4])
        month = int(line[5:7])
        day = int(line[8:10])
        hour = int(line[11:13])
        minute = int(line[14:16])
        second = int(line[17:19])
        milliseconds = int(line[20:23])
        utcoffset_hours = line[23:26]
        utcoffset_minutes = line[26:28]
        d = datetime(year, month, day, hour, minute, second, milliseconds * 1000)
        return d


class serializable(object):
    def __init__(self, name=None, type=None, list=False, date_format=DateFormatIso8601):
        self.name = name
        self.type = type
        self.list = list
        self.date_format = date_format

    def __call__(self, method):
        method.func_dict['serializable'] = self
        return method


class DefaultObject(object):
    def __init__(self):
        super(DefaultObject, self).__init__()
        self._field_map = dict()

    def __str__(self):
        s = u"%s {" % type(self).__name__
        first = True
        property_names = [p for p in dir(type(self)) if isinstance(getattr(type(self), p), property)]
        for k in property_names:
            if not first:
                s += u", "
            else:
                first = False

            v = getattr(self, k)
            if isinstance(v, list):
                s += u"%s=[" % k
                f = True
                for o in v:
                    if not f:
                        s += u", "
                    f = False
                    s += u"%s" % o
                s += u"]"
            elif isinstance(v, unicode):
                s += k + u"=\"" + v + u"\""
            else:
                s += unicode(k) + u"=" + unicode(v)

        s += u"}"

        return s

    def get_value(self, serializable, o):
        if not isinstance(o, datetime):
            return o
        date_format = DateFormatIso8601
        if serializable and serializable.date_format:
            date_format = serializable.date_format

        return date_format.strftime(o)

    @classmethod
    def set_value(cls, field_name, serializable, o, v):
        setattr(o, field_name, cls.deserialize(field_name, serializable, v))

    @classmethod
    def deserialize(cls, field_name, serializable, v):
        if isinstance(v, list):
            res = []
            for o in v:
                res.append(cls.deserialize(None, serializable, o))
            return res

        if isinstance(v, dict):
            if serializable.type == basestring:
                return unicode(v)
            o = serializable.type()
            for p in dir(type(o)):
                attr = getattr(type(o), p)
                if not isinstance(attr, property):
                    continue

                serializable = attr.fget.func_dict['serializable']
                k = serializable.name
                if not k:
                    k = attr.fget.__name__
                v1 = v.get(k)

                type(o).set_value(p, serializable, o, v1)

            return o

        if field_name and cls.isdate(field_name):
            date_format = DateFormatIso8601
            if serializable and serializable.date_format:
                date_format = serializable.date_format
            return date_format.strptime(v)

        return v

    def to_dict(self):
        dict = {}
        for p in dir(type(self)):
            attr = getattr(type(self), p)
            if not isinstance(attr, property):
                continue
            serializable = attr.fget.func_dict['serializable']
            k = serializable.name
            if not k:
                k = attr.fget.__name__
            attr1 = getattr(self, p)

            # Do not serialize None values
            if not attr1:
                continue

            if isinstance(attr1, list):
                dict[k] = []
                for a in attr1:
                    if hasattr(a, "to_dict"):
                        dict[k].append(a.to_dict())
                    else:
                        dict[k].append(self.get_value(serializable, a))
            else:
                if hasattr(attr1, "to_dict"):
                    dict[k] = attr1.to_dict()
                else:
                    dict[k] = self.get_value(serializable, attr1)
        return dict

    def to_JSON(self):
        dict = self.to_dict()
        return json.dumps(self, default=lambda o: dict, check_circular=False)

    def islist(self, fieldName):
        attr = getattr(type(self), fieldName)
        serializable = attr.fget.func_dict['serializable']
        is_list = serializable and serializable.list
        if not is_list:
            return False

        return is_list

    @classmethod
    def isdate(cls, fieldName):
        attr = getattr(cls, fieldName)
        serializable = attr.fget.func_dict['serializable']
        is_date = serializable and (serializable.type == datetime)
        if not is_date:
            return False

        return is_date

    def get_field_value(self, field_name):
        return self._field_map.get(field_name)

    def set_field_value(self, field_name, field_value):
        self._field_map[field_name] = field_value

    @classmethod
    def from_JSON(cls, s):
        vals = json.JSONDecoder().decode(s)

        o = cls()
        for p in dir(type(o)):
            attr = getattr(type(o), p)
            if not isinstance(attr, property):
                continue

            serializable = attr.fget.func_dict['serializable']
            k = serializable.name
            if not k:
                k = attr.fget.__name__
            v = vals.get(k)

            cls.set_value(p, serializable, o, v)

        return o
