#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the PyObject representing the Python list.
 */

void print_python_list(PyObject *p)
{
if (!PyList_Check(p))
{
fprintf(stderr, "Invalid PyListObject\n");
return;
}

Py_ssize_t size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);

printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (Py_ssize_t i = 0; i < size; i++)
{
PyObject *item = PyList_GetItem(p, i);
const char *item_type = item->ob_type->tp_name;
printf("Element %ld: %s\n", i, item_type);
}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the PyObject representing the Python bytes.
 */

void print_python_bytes(PyObject *p)
{
if (!PyBytes_Check(p))
{
fprintf(stderr, "Invalid PyBytesObject\n");
return;
}

Py_ssize_t size = PyBytes_Size(p);
const char *str = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

if (size > 10)
size = 10;
printf("  first %ld bytes: ", size);
for (Py_ssize_t i = 0; i < size; i++)
{
printf("%02hhx", str[i]);
if (i < size - 1)
printf(" ");
}
printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: Pointer to the PyObject representing the Python float.
 */

void print_python_float(PyObject *p)
{
if (!PyFloat_Check(p))
{
fprintf(stderr, "Invalid PyFloatObject\n");
return;
}

double value = PyFloat_AsDouble(p);

printf("[.] float object info\n");
printf("  value: %f\n", value);
}
