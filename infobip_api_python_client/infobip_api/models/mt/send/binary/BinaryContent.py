# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
class BinaryContent(DefaultObject):
    @property
    @serializable(name="dataCoding", type=int)
    def data_coding(self):
        return self.get_field_value("data_coding")

    @data_coding.setter
    def data_coding(self, data_coding):
        self.set_field_value("data_coding", data_coding)

    def set_data_coding(self, data_coding):
        self.data_coding = data_coding
        return self

    @property
    @serializable(name="hex", type=unicode)
    def hex(self):
        return self.get_field_value("hex")

    @hex.setter
    def hex(self, hex):
        self.set_field_value("hex", hex)

    def set_hex(self, hex):
        self.hex = hex
        return self

    @property
    @serializable(name="esmClass", type=int)
    def esm_class(self):
        return self.get_field_value("esm_class")

    @esm_class.setter
    def esm_class(self, esm_class):
        self.set_field_value("esm_class", esm_class)

    def set_esm_class(self, esm_class):
        self.esm_class = esm_class
        return self