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
/* Check if the object is a string */
if (!PyUnicode_Check(p))
{
printf("Error: Object is not a valid string.\n");
return;
}
/* Get the string value from the object */
PyObject *strValue = PyUnicode_AsUTF8String(p);
if (strValue == NULL)
{
printf("Error: Failed to get string value.\n");
return;
}
/* Get the C string pointer from the string value */
const char *cStr = PyBytes_AsString(strValue);
if (cStr == NULL)
{
printf("Error: Failed to get C string.\n");
Py_DECREF(strValue);
return;
}
/* Print the string */
printf("%s\n", cStr);
/* Cleanup */
Py_DECREF(strValue);
}
