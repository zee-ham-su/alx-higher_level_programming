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
  if (!PyBytes_Check(obj))
    {
      printf("  [ERROR] Invalid Bytes Object\n");
      return;
    }

  length = ((PyVarObject *)(obj))->ob_size;
  str = ((PyBytesObject *)obj)->ob_sval;

  printf("  size: %ld\n", length);
  printf("  trying string: %s\n", str);

  if (length >= 10)
    limit = 10;
  else
    limit = length + 1;

  printf("  first %ld bytes:", limit);

  for (i = 0; i < limit; i++)
    {
      if (str[i] >= 0)
	printf(" %02x", str[i]);
      else
	printf(" %02x", 256 + str[i]);
    }

  printf("\n");
 }
 

 /**
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
      item = ((PyListObject *)obj)->ob_item[i];
      printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
      if (PyBytes_Check(item))
	print_python_bytes(item);
    }
 }
