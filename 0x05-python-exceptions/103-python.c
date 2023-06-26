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
printf("[ERROR] Invalid PyListObject\n");
return;
}

Py_ssize_t size = PyList_Size(p);
Py_ssize_t allocated = ((PyListObject *)p)->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);

for (Py_ssize_t i = 0; i < size; i++)
{
PyObject *item = PyList_GetItem(p, i);
const char *item_type = Py_TYPE(item)->tp_name;
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
printf("[ERROR] Invalid Bytes Object\n");
return;
}

Py_ssize_t size = PyBytes_GET_SIZE(p);
const char *bytes_data = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", bytes_data);
printf("  first 6 bytes: ");

Py_ssize_t limit = size > 6 ? 6 : size;
for (Py_ssize_t i = 0; i < limit; i++)
{
printf("%02hhx", bytes_data[i]);
if (i < limit - 1)
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
printf("[ERROR] Invalid Float Object\n");
return;
}

double value = PyFloat_AS_DOUBLE(p);

printf("[.] float object info\n");
printf("  value: %f\n", value);
}
