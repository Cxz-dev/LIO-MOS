# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from livox_ros_driver/CustomPoint.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CustomPoint(genpy.Message):
  _md5sum = "109a3cc548bb1f96626be89a5008bd6d"
  _type = "livox_ros_driver/CustomPoint"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Livox costom pointcloud format.

uint32 offset_time      # offset time relative to the base time
float32 x               # X axis, unit:m
float32 y               # Y axis, unit:m
float32 z               # Z axis, unit:m
uint8 reflectivity      # reflectivity, 0~255
uint8 tag               # livox tag
uint8 line              # laser number in lidar

"""
  __slots__ = ['offset_time','x','y','z','reflectivity','tag','line']
  _slot_types = ['uint32','float32','float32','float32','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       offset_time,x,y,z,reflectivity,tag,line

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CustomPoint, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.offset_time is None:
        self.offset_time = 0
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.z is None:
        self.z = 0.
      if self.reflectivity is None:
        self.reflectivity = 0
      if self.tag is None:
        self.tag = 0
      if self.line is None:
        self.line = 0
    else:
      self.offset_time = 0
      self.x = 0.
      self.y = 0.
      self.z = 0.
      self.reflectivity = 0
      self.tag = 0
      self.line = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_I3f3B().pack(_x.offset_time, _x.x, _x.y, _x.z, _x.reflectivity, _x.tag, _x.line))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 19
      (_x.offset_time, _x.x, _x.y, _x.z, _x.reflectivity, _x.tag, _x.line,) = _get_struct_I3f3B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_I3f3B().pack(_x.offset_time, _x.x, _x.y, _x.z, _x.reflectivity, _x.tag, _x.line))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 19
      (_x.offset_time, _x.x, _x.y, _x.z, _x.reflectivity, _x.tag, _x.line,) = _get_struct_I3f3B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_I3f3B = None
def _get_struct_I3f3B():
    global _struct_I3f3B
    if _struct_I3f3B is None:
        _struct_I3f3B = struct.Struct("<I3f3B")
    return _struct_I3f3B
