using System;

namespace LR_053506_Slutski_Lab6.Exceptions
{
    public class CustomCollectionException : InvalidOperationException
    {
        public CustomCollectionException(string message)
            : base(message)
        {
        }
    }
}