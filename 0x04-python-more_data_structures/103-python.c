#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: PyObject pointer to the Python list
 */

void print_python_list(PyObject *p)
{
Py_ssize_t list_size, i;
PyObject *list_item;

list_size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", list_size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
for (i = 0; i < list_size; i++)
{
list_item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(list_item)->tp_name);
if (PyBytes_Check(list_item))
print_python_bytes(list_item);
}
}

 /**
  * print_python_bytes - Prints information about a Python bytes object
  * @p: PyObject pointer to the Python bytes object
  */

void print_python_bytes(PyObject *p)
{
Py_ssize_t bytes_size, i;
char *bytes_string;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

bytes_size = PyBytes_Size(p);
bytes_string = PyBytes_AsString(p);

printf("  size: %zd\n", bytes_size);
printf("  trying string: %s\n", bytes_string);

printf("  first %zd bytes:", bytes_size + 1 > 10 ? 10 : bytes_size + 1);
for (i = 0; i < bytes_size + 1 && i < 10; i++)
printf(" %02hhx", bytes_string[i]);
printf("\n");
}
