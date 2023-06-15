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

  printf("[.] bytes object info\n");

  if (!PyBytes_Check(p))
    {
      printf("  [ERROR] Invalid Bytes Object\n");
      return;
    }

  length = ((PyVarObject *)(p))->ob_size;
  str = ((PyBytesObject *)p)->ob_sval;

  printf("  size: %ld\n", length);
  printf("  trying string: %s\n", str);


  limit = (length >= 10) ? 10 : (length + 1);
  printf("  first %ld bytes:", limit);

  for (i = 0; i < limit; i++)
    printf(" %02x", str[i] >= 0 ? str[i] : 256 + str[i]);
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

   length = PyList_Size(p);
   list_obj = (PyListObject *)p;

   printf("[*] Python list info\n");
   printf("[*] Size of the Python List = %ld\n", length);
   printf("[*] Allocated = %ld\n", list_obj->allocated);

   for (i = 0; i < length; i++)
     {
       item = PyList_GetItem(p, i);
       printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
       if (PyBytes_Check(item))
	 print_python_bytes(item);
     }

 }
