#include <Python.h>
#include <object.h>
#include <listobject.h>

/**                                                                
 * print_python_list_info - prints some basic information on        
 * python list                                                      
 * @p: python object                                                
 */

void print_python_list_info(PyObject *p)
{
long int list_size = PyList_Size(p);
int i;
PyListObject *list_obj = (PyListObject *)p;

printf("[*] Size of the Python List = %li\n", list_size);
printf("[*] Allocated = %li\n", list_obj->allocated);

for (i = 0; i < list_size; i++)
{
PyObject *element = list_obj->ob_item[i];
const char *type_name = Py_TYPE(element)->tp_name;
printf("Element %i: %s\n", i, type_name);
}
}
