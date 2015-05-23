#include "python.h" 

int  main(int  argc, char * argv[])
{
    Py_Initialize();
    PyRun_SimpleString("print( " Hello World " )" );
    Py_Finalize();
    system("PAUSE" );
    return  0 ;
}
