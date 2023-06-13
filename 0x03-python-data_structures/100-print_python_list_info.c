#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Function to print basic
 * information about Python lists
 * @p: PyObject pointer to the Python list
 */

void print_python_list_info(PyObject *p)
{
long int size = PyList_Size(p);
int i;
for (i = 0; i < size; i++)
{
PyObject *element = PyList_GET_ITEM(p, i);
const char *typeName = element->ob_type->tp_name;
printf("Element %d: %s\n", i, typeName);
}

printf("[*] Size of the Python List = %ld\n", size);
 
long int allocated = ((PyListObject *)p)->allocated;
printf("[*] Allocated = %ld\n", allocated);
}
