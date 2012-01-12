# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyncptl', [dirname(__file__)])
        except ImportError:
            import _pyncptl
            return _pyncptl
        if fp is not None:
            try:
                _mod = imp.load_module('_pyncptl', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyncptl = swig_import_helper()
    del swig_import_helper
else:
    import _pyncptl
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def ncptl_fatal(*args):
  return _pyncptl.ncptl_fatal(*args)
ncptl_fatal = _pyncptl.ncptl_fatal

def ncptl_allocate_timing_flag():
  return _pyncptl.ncptl_allocate_timing_flag()
ncptl_allocate_timing_flag = _pyncptl.ncptl_allocate_timing_flag

def ncptl_reset_timing_flag(*args):
  return _pyncptl.ncptl_reset_timing_flag(*args)
ncptl_reset_timing_flag = _pyncptl.ncptl_reset_timing_flag

def ncptl_test_timing_flag(*args):
  return _pyncptl.ncptl_test_timing_flag(*args)
ncptl_test_timing_flag = _pyncptl.ncptl_test_timing_flag

def ncptl_free_timing_flag(*args):
  return _pyncptl.ncptl_free_timing_flag(*args)
ncptl_free_timing_flag = _pyncptl.ncptl_free_timing_flag
NCPTL_RUN_TIME_VERSION = _pyncptl.NCPTL_RUN_TIME_VERSION
PRId64 = _pyncptl.PRId64
PRIu64 = _pyncptl.PRIu64
PRIx64 = _pyncptl.PRIx64
NICS = _pyncptl.NICS
NCPTL_FUNC_NO_AGGREGATE = _pyncptl.NCPTL_FUNC_NO_AGGREGATE
NCPTL_FUNC_MEAN = _pyncptl.NCPTL_FUNC_MEAN
NCPTL_FUNC_HARMONIC_MEAN = _pyncptl.NCPTL_FUNC_HARMONIC_MEAN
NCPTL_FUNC_GEOMETRIC_MEAN = _pyncptl.NCPTL_FUNC_GEOMETRIC_MEAN
NCPTL_FUNC_MEDIAN = _pyncptl.NCPTL_FUNC_MEDIAN
NCPTL_FUNC_MAD = _pyncptl.NCPTL_FUNC_MAD
NCPTL_FUNC_STDEV = _pyncptl.NCPTL_FUNC_STDEV
NCPTL_FUNC_VARIANCE = _pyncptl.NCPTL_FUNC_VARIANCE
NCPTL_FUNC_SUM = _pyncptl.NCPTL_FUNC_SUM
NCPTL_FUNC_MINIMUM = _pyncptl.NCPTL_FUNC_MINIMUM
NCPTL_FUNC_MAXIMUM = _pyncptl.NCPTL_FUNC_MAXIMUM
NCPTL_FUNC_FINAL = _pyncptl.NCPTL_FUNC_FINAL
NCPTL_FUNC_ONLY = _pyncptl.NCPTL_FUNC_ONLY
NCPTL_FUNC_HISTOGRAM = _pyncptl.NCPTL_FUNC_HISTOGRAM

def ncptl_init(*args):
  return _pyncptl.ncptl_init(*args)
ncptl_init = _pyncptl.ncptl_init

def ncptl_finalize():
  return _pyncptl.ncptl_finalize()
ncptl_finalize = _pyncptl.ncptl_finalize

def ncptl_fill_buffer(*args):
  return _pyncptl.ncptl_fill_buffer(*args)
ncptl_fill_buffer = _pyncptl.ncptl_fill_buffer

def ncptl_verify(*args):
  return _pyncptl.ncptl_verify(*args)
ncptl_verify = _pyncptl.ncptl_verify

def ncptl_permit_signal(*args):
  return _pyncptl.ncptl_permit_signal(*args)
ncptl_permit_signal = _pyncptl.ncptl_permit_signal

def ncptl_parse_command_line(*args):
  return _pyncptl.ncptl_parse_command_line(*args)
ncptl_parse_command_line = _pyncptl.ncptl_parse_command_line

def ncptl_time():
  return _pyncptl.ncptl_time()
ncptl_time = _pyncptl.ncptl_time

def ncptl_set_flag_after_usecs(*args):
  return _pyncptl.ncptl_set_flag_after_usecs(*args)
ncptl_set_flag_after_usecs = _pyncptl.ncptl_set_flag_after_usecs

def ncptl_udelay(*args):
  return _pyncptl.ncptl_udelay(*args)
ncptl_udelay = _pyncptl.ncptl_udelay

def ncptl_seed_random_task(*args):
  return _pyncptl.ncptl_seed_random_task(*args)
ncptl_seed_random_task = _pyncptl.ncptl_seed_random_task

def ncptl_random_task(*args):
  return _pyncptl.ncptl_random_task(*args)
ncptl_random_task = _pyncptl.ncptl_random_task

def ncptl_allocate_task_map(*args):
  return _pyncptl.ncptl_allocate_task_map(*args)
ncptl_allocate_task_map = _pyncptl.ncptl_allocate_task_map

def ncptl_virtual_to_physical(*args):
  return _pyncptl.ncptl_virtual_to_physical(*args)
ncptl_virtual_to_physical = _pyncptl.ncptl_virtual_to_physical

def ncptl_physical_to_virtual(*args):
  return _pyncptl.ncptl_physical_to_virtual(*args)
ncptl_physical_to_virtual = _pyncptl.ncptl_physical_to_virtual

def ncptl_assign_processor(*args):
  return _pyncptl.ncptl_assign_processor(*args)
ncptl_assign_processor = _pyncptl.ncptl_assign_processor

def ncptl_malloc(*args):
  return _pyncptl.ncptl_malloc(*args)
ncptl_malloc = _pyncptl.ncptl_malloc

def ncptl_free(*args):
  return _pyncptl.ncptl_free(*args)
ncptl_free = _pyncptl.ncptl_free

def ncptl_realloc(*args):
  return _pyncptl.ncptl_realloc(*args)
ncptl_realloc = _pyncptl.ncptl_realloc

def ncptl_malloc_message(*args):
  return _pyncptl.ncptl_malloc_message(*args)
ncptl_malloc_message = _pyncptl.ncptl_malloc_message

def ncptl_malloc_misaligned(*args):
  return _pyncptl.ncptl_malloc_misaligned(*args)
ncptl_malloc_misaligned = _pyncptl.ncptl_malloc_misaligned

def ncptl_get_message_buffer(*args):
  return _pyncptl.ncptl_get_message_buffer(*args)
ncptl_get_message_buffer = _pyncptl.ncptl_get_message_buffer

def ncptl_touch_data(*args):
  return _pyncptl.ncptl_touch_data(*args)
ncptl_touch_data = _pyncptl.ncptl_touch_data

def ncptl_touch_memory(*args):
  return _pyncptl.ncptl_touch_memory(*args)
ncptl_touch_memory = _pyncptl.ncptl_touch_memory

def ncptl_log_add_comment(*args):
  return _pyncptl.ncptl_log_add_comment(*args)
ncptl_log_add_comment = _pyncptl.ncptl_log_add_comment

def ncptl_log_open(*args):
  return _pyncptl.ncptl_log_open(*args)
ncptl_log_open = _pyncptl.ncptl_log_open

def ncptl_log_lookup_string(*args):
  return _pyncptl.ncptl_log_lookup_string(*args)
ncptl_log_lookup_string = _pyncptl.ncptl_log_lookup_string

def ncptl_log_generate_uuid():
  return _pyncptl.ncptl_log_generate_uuid()
ncptl_log_generate_uuid = _pyncptl.ncptl_log_generate_uuid

def ncptl_log_write(*args):
  return _pyncptl.ncptl_log_write(*args)
ncptl_log_write = _pyncptl.ncptl_log_write

def ncptl_log_write_prologue(*args):
  return _pyncptl.ncptl_log_write_prologue(*args)
ncptl_log_write_prologue = _pyncptl.ncptl_log_write_prologue

def ncptl_log_write_epilogue(*args):
  return _pyncptl.ncptl_log_write_epilogue(*args)
ncptl_log_write_epilogue = _pyncptl.ncptl_log_write_epilogue

def ncptl_log_compute_aggregates(*args):
  return _pyncptl.ncptl_log_compute_aggregates(*args)
ncptl_log_compute_aggregates = _pyncptl.ncptl_log_compute_aggregates

def ncptl_log_commit_data(*args):
  return _pyncptl.ncptl_log_commit_data(*args)
ncptl_log_commit_data = _pyncptl.ncptl_log_commit_data

def ncptl_log_get_contents(*args):
  return _pyncptl.ncptl_log_get_contents(*args)
ncptl_log_get_contents = _pyncptl.ncptl_log_get_contents

def ncptl_log_close(*args):
  return _pyncptl.ncptl_log_close(*args)
ncptl_log_close = _pyncptl.ncptl_log_close

def ncptl_func_sqrt(*args):
  return _pyncptl.ncptl_func_sqrt(*args)
ncptl_func_sqrt = _pyncptl.ncptl_func_sqrt

def ncptl_dfunc_sqrt(*args):
  return _pyncptl.ncptl_dfunc_sqrt(*args)
ncptl_dfunc_sqrt = _pyncptl.ncptl_dfunc_sqrt

def ncptl_func_cbrt(*args):
  return _pyncptl.ncptl_func_cbrt(*args)
ncptl_func_cbrt = _pyncptl.ncptl_func_cbrt

def ncptl_dfunc_cbrt(*args):
  return _pyncptl.ncptl_dfunc_cbrt(*args)
ncptl_dfunc_cbrt = _pyncptl.ncptl_dfunc_cbrt

def ncptl_func_root(*args):
  return _pyncptl.ncptl_func_root(*args)
ncptl_func_root = _pyncptl.ncptl_func_root

def ncptl_dfunc_root(*args):
  return _pyncptl.ncptl_dfunc_root(*args)
ncptl_dfunc_root = _pyncptl.ncptl_dfunc_root

def ncptl_func_bits(*args):
  return _pyncptl.ncptl_func_bits(*args)
ncptl_func_bits = _pyncptl.ncptl_func_bits

def ncptl_dfunc_bits(*args):
  return _pyncptl.ncptl_dfunc_bits(*args)
ncptl_dfunc_bits = _pyncptl.ncptl_dfunc_bits

def ncptl_func_shift_left(*args):
  return _pyncptl.ncptl_func_shift_left(*args)
ncptl_func_shift_left = _pyncptl.ncptl_func_shift_left

def ncptl_dfunc_shift_left(*args):
  return _pyncptl.ncptl_dfunc_shift_left(*args)
ncptl_dfunc_shift_left = _pyncptl.ncptl_dfunc_shift_left

def ncptl_func_log10(*args):
  return _pyncptl.ncptl_func_log10(*args)
ncptl_func_log10 = _pyncptl.ncptl_func_log10

def ncptl_dfunc_log10(*args):
  return _pyncptl.ncptl_dfunc_log10(*args)
ncptl_dfunc_log10 = _pyncptl.ncptl_dfunc_log10

def ncptl_func_factor10(*args):
  return _pyncptl.ncptl_func_factor10(*args)
ncptl_func_factor10 = _pyncptl.ncptl_func_factor10

def ncptl_dfunc_factor10(*args):
  return _pyncptl.ncptl_dfunc_factor10(*args)
ncptl_dfunc_factor10 = _pyncptl.ncptl_dfunc_factor10

def ncptl_func_abs(*args):
  return _pyncptl.ncptl_func_abs(*args)
ncptl_func_abs = _pyncptl.ncptl_func_abs

def ncptl_dfunc_abs(*args):
  return _pyncptl.ncptl_dfunc_abs(*args)
ncptl_dfunc_abs = _pyncptl.ncptl_dfunc_abs

def ncptl_func_power(*args):
  return _pyncptl.ncptl_func_power(*args)
ncptl_func_power = _pyncptl.ncptl_func_power

def ncptl_dfunc_power(*args):
  return _pyncptl.ncptl_dfunc_power(*args)
ncptl_dfunc_power = _pyncptl.ncptl_dfunc_power

def ncptl_func_modulo(*args):
  return _pyncptl.ncptl_func_modulo(*args)
ncptl_func_modulo = _pyncptl.ncptl_func_modulo

def ncptl_dfunc_modulo(*args):
  return _pyncptl.ncptl_dfunc_modulo(*args)
ncptl_dfunc_modulo = _pyncptl.ncptl_dfunc_modulo

def ncptl_func_floor(*args):
  return _pyncptl.ncptl_func_floor(*args)
ncptl_func_floor = _pyncptl.ncptl_func_floor

def ncptl_dfunc_floor(*args):
  return _pyncptl.ncptl_dfunc_floor(*args)
ncptl_dfunc_floor = _pyncptl.ncptl_dfunc_floor

def ncptl_func_ceiling(*args):
  return _pyncptl.ncptl_func_ceiling(*args)
ncptl_func_ceiling = _pyncptl.ncptl_func_ceiling

def ncptl_dfunc_ceiling(*args):
  return _pyncptl.ncptl_dfunc_ceiling(*args)
ncptl_dfunc_ceiling = _pyncptl.ncptl_dfunc_ceiling

def ncptl_func_round(*args):
  return _pyncptl.ncptl_func_round(*args)
ncptl_func_round = _pyncptl.ncptl_func_round

def ncptl_dfunc_round(*args):
  return _pyncptl.ncptl_dfunc_round(*args)
ncptl_dfunc_round = _pyncptl.ncptl_dfunc_round

def ncptl_func_tree_parent(*args):
  return _pyncptl.ncptl_func_tree_parent(*args)
ncptl_func_tree_parent = _pyncptl.ncptl_func_tree_parent

def ncptl_dfunc_tree_parent(*args):
  return _pyncptl.ncptl_dfunc_tree_parent(*args)
ncptl_dfunc_tree_parent = _pyncptl.ncptl_dfunc_tree_parent

def ncptl_func_tree_child(*args):
  return _pyncptl.ncptl_func_tree_child(*args)
ncptl_func_tree_child = _pyncptl.ncptl_func_tree_child

def ncptl_dfunc_tree_child(*args):
  return _pyncptl.ncptl_dfunc_tree_child(*args)
ncptl_dfunc_tree_child = _pyncptl.ncptl_dfunc_tree_child

def ncptl_func_mesh_coord(*args):
  return _pyncptl.ncptl_func_mesh_coord(*args)
ncptl_func_mesh_coord = _pyncptl.ncptl_func_mesh_coord

def ncptl_dfunc_mesh_coord(*args):
  return _pyncptl.ncptl_dfunc_mesh_coord(*args)
ncptl_dfunc_mesh_coord = _pyncptl.ncptl_dfunc_mesh_coord

def ncptl_func_mesh_neighbor(*args):
  return _pyncptl.ncptl_func_mesh_neighbor(*args)
ncptl_func_mesh_neighbor = _pyncptl.ncptl_func_mesh_neighbor

def ncptl_dfunc_mesh_neighbor(*args):
  return _pyncptl.ncptl_dfunc_mesh_neighbor(*args)
ncptl_dfunc_mesh_neighbor = _pyncptl.ncptl_dfunc_mesh_neighbor

def ncptl_func_mesh_distance(*args):
  return _pyncptl.ncptl_func_mesh_distance(*args)
ncptl_func_mesh_distance = _pyncptl.ncptl_func_mesh_distance

def ncptl_dfunc_mesh_distance(*args):
  return _pyncptl.ncptl_dfunc_mesh_distance(*args)
ncptl_dfunc_mesh_distance = _pyncptl.ncptl_dfunc_mesh_distance

def ncptl_func_knomial_parent(*args):
  return _pyncptl.ncptl_func_knomial_parent(*args)
ncptl_func_knomial_parent = _pyncptl.ncptl_func_knomial_parent

def ncptl_dfunc_knomial_parent(*args):
  return _pyncptl.ncptl_dfunc_knomial_parent(*args)
ncptl_dfunc_knomial_parent = _pyncptl.ncptl_dfunc_knomial_parent

def ncptl_func_knomial_child(*args):
  return _pyncptl.ncptl_func_knomial_child(*args)
ncptl_func_knomial_child = _pyncptl.ncptl_func_knomial_child

def ncptl_dfunc_knomial_child(*args):
  return _pyncptl.ncptl_dfunc_knomial_child(*args)
ncptl_dfunc_knomial_child = _pyncptl.ncptl_dfunc_knomial_child

def ncptl_func_random_uniform(*args):
  return _pyncptl.ncptl_func_random_uniform(*args)
ncptl_func_random_uniform = _pyncptl.ncptl_func_random_uniform

def ncptl_dfunc_random_uniform(*args):
  return _pyncptl.ncptl_dfunc_random_uniform(*args)
ncptl_dfunc_random_uniform = _pyncptl.ncptl_dfunc_random_uniform

def ncptl_func_random_gaussian(*args):
  return _pyncptl.ncptl_func_random_gaussian(*args)
ncptl_func_random_gaussian = _pyncptl.ncptl_func_random_gaussian

def ncptl_dfunc_random_gaussian(*args):
  return _pyncptl.ncptl_dfunc_random_gaussian(*args)
ncptl_dfunc_random_gaussian = _pyncptl.ncptl_dfunc_random_gaussian

def ncptl_func_random_poisson(*args):
  return _pyncptl.ncptl_func_random_poisson(*args)
ncptl_func_random_poisson = _pyncptl.ncptl_func_random_poisson

def ncptl_dfunc_random_poisson(*args):
  return _pyncptl.ncptl_dfunc_random_poisson(*args)
ncptl_dfunc_random_poisson = _pyncptl.ncptl_dfunc_random_poisson

def ncptl_func_random_pareto(*args):
  return _pyncptl.ncptl_func_random_pareto(*args)
ncptl_func_random_pareto = _pyncptl.ncptl_func_random_pareto

def ncptl_dfunc_random_pareto(*args):
  return _pyncptl.ncptl_dfunc_random_pareto(*args)
ncptl_dfunc_random_pareto = _pyncptl.ncptl_dfunc_random_pareto

cvar = _pyncptl.cvar

