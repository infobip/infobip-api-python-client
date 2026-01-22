import io
import os
from typing import Optional, Union
from pydantic import BaseModel, ConfigDict


class FileParameter(BaseModel):
    """
    Represents a file passed to an API as a parameter.
    Supports raw bytes or file-like streams (binary).
    """

    content: io.IOBase
    name: str = "attachment"
    content_type: str = "application/octet-stream"

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(
        self,
        content: Union[bytes, io.IOBase],
        name: Optional[str] = None,
        content_type: Optional[str] = None,
    ):
        """
        Initialize FileParameter with content, name, and content_type.

        :param content: Raw bytes or file-like binary stream (IOBase).
        :param name: Optional filename.
        :param content_type: Optional MIME type, defaults to 'application/octet-stream'.
        """
        if isinstance(content, bytes):
            content = io.BytesIO(content)

        if not isinstance(content, io.IOBase):
            raise TypeError("content must be bytes or a file-like IOBase stream")

        inferred_name = name or getattr(content, "name", None)
        if inferred_name:
            inferred_name = os.path.basename(inferred_name)
        else:
            inferred_name = "attachment"

        super().__init__(
            content=content,
            name=inferred_name,
            content_type=content_type or "application/octet-stream",
        )

    def __repr__(self):
        return f"<FileParameter name={self.name!r}, content_type={self.content_type!r}>"
