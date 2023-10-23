#include <Python.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */

void print_python_list(PyObject *p)
{

if (!PyList_Check(p))
{
printf(stderr, "[ERROR] Invalid List Object\n");
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
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
