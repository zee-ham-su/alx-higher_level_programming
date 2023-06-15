#include <stdio.h>
#include <Python.h>



/**
 * print_python_bytes - Prints information about a Python
 * bytes object
 * @p: PyObject pointer to the Python bytes object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
char *str;
long int length, i, limit;
unsigned char byte:
printf("[.] bytes object info\n");
if (Py_TYPE(obj) != &PyBytes_Type)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

length = ((PyVarObject *)(obj))->ob_size;
str = ((PyBytesObject *)obj)->ob_sval;

printf("  size: %ld\n", length);
printf("  trying string: %s\n", str);


limit = (length >= 10) ? 10 : (length + 1);
printf("  first %ld bytes:", limit);

for (i = 0; i < limit; i++)
{
byte = str[i];
printf(" %02x", byte);
}

printf("\n");
}


/**
 * print_python_list - Prints information about a Python list
 * @p: PyObject pointer to the Python list
 * Return: no return
 */

void print_python_list(PyObject *p)
{
long int length, i;
PyListObject *list_obj;
PyObject *item;

length = ((PyVarObject *)(obj))->ob_size;
list_obj = (PyListObject *)obj;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", length);
printf("[*] Allocated = %ld\n", list_obj->allocated);

for (i = 0; i < length; i++)
{
item = PyList_GetItem(obj, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
if (PyBytes_Check(item))
print_python_bytes(item);
}

}
