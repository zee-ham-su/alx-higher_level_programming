#include "Python.h"


/**
 * print_python_string - Prints a Python string.
 * @p: The PyObject pointer to the Python object.
 *
 * This function takes a PyObject pointer representing a Python
 * object and
 * checks if it is a valid string. If it is a string,
 * it prints the string value.
 * If it is not a string, it prints an error message.
 */


void print_python_string(PyObject *p)
{

PyObject *str, *repr;

(void)repr;
printf("[.] string object info\n");

if (strcmp(p->ob_type->tp_name, "str"))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

if (PyUnicode_IS_COMPACT_ASCII(p))
printf("  type: compact ascii\n");
else
printf("  type: compact unicode object\n");

repr = PyObject_Repr(p);
str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
printf("  value: %s\n", PyBytes_AsString(str));
}
