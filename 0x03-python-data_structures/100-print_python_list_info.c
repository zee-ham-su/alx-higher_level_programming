#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Function to print basic
 * information about Python lists
 * @p: PyObject pointer to the Python list
 */

void print_python_list_info(PyObject *p)
{
Py_ssize_t size = PyList_GET_SIZE(p);
Py_ssize_t allocated = ((PyListObject *)p)->allocated;

for (Py_ssize_t i = 0; i < size; i++)
{
PyObject *element = PyList_GET_ITEM(p, i);
const char *typeName = element->ob_type->tp_name;
printf("Element %ld: %s\n", i, typeName);
}

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);
}
