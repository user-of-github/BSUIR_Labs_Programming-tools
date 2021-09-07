using LR_053506_Slutski_Lab5.Interfaces;

namespace LR_053506_Slutski_Lab5.Collections
{
    public class CustomCollection<TValueType> : ICustomCollection<TValueType> where TValueType : class
    {
        private class CustomCollectionNode
        {
            public CustomCollectionNode PreviousNode;
            public TValueType CurrentNode;
            public CustomCollectionNode NextNode;

            public CustomCollectionNode(
                CustomCollectionNode previous,
                TValueType current,
                CustomCollectionNode next
            ) => (PreviousNode, CurrentNode, NextNode) = (previous, current, next);
        }


        private CustomCollectionNode _firstItem;
        private CustomCollectionNode _lastItem;
        private CustomCollectionNode _currentItem;
        private ushort _size;

        public TValueType this[ushort index]
        {
            get => FindByIndex(index).CurrentNode;
            set => FindByIndex(index).CurrentNode = value;
        }

        public CustomCollection() => Clear();

        public void Reset() => _currentItem = _size > 0 ? _firstItem : null;

        public void Next() => _currentItem = _currentItem.NextNode;

        public TValueType Current() => _currentItem.CurrentNode;

        public ushort Count => _size;

        public void Add(TValueType item)
        {
            var newNode = new CustomCollectionNode(null, item, null);
            if (_size == 0)
            {
                _firstItem = _currentItem = newNode;
            }
            else
            {
                newNode.PreviousNode = _lastItem;
                _lastItem.NextNode = newNode;
            }

            _lastItem = newNode;
            ++_size;
        }

        public void Remove(TValueType item)
        {
            var found = FindByValue(item);
            if (found == null)
                return;

            RemoveByPointer(found);
        }

        public TValueType RemoveCurrent()
        {
            var current = _currentItem?.CurrentNode;
            var following = _currentItem?.NextNode;
            RemoveByPointer(_currentItem);
            _currentItem = following;
            return current;
        }

        private void RemoveByPointer(CustomCollectionNode found)
        {
            if (found.PreviousNode == null) // it is first element 
            {
                _firstItem = _firstItem.NextNode;
                if (_firstItem != null)
                    _firstItem.PreviousNode = null;
                if (_size <= 2)
                    _lastItem = _firstItem;
            }
            else if (found.NextNode == null) // it is last element
            {
                _lastItem = _lastItem.PreviousNode;
                if (_lastItem != null)
                    _lastItem.NextNode = null;
                if (_size <= 2)
                    _firstItem = _lastItem;
            }
            else
            {
                var previous = found.PreviousNode;
                var following = found.NextNode;
                previous.NextNode = following;
                following.PreviousNode = previous;
            }

            --_size;
        }

        private void Clear()
        {
            _firstItem = null;
            _lastItem = null;
            _currentItem = null;
            _size = 0;
        }

        private CustomCollectionNode FindByValue(TValueType toFind)
        {
            var element = _firstItem;
            while (element != null && element.CurrentNode != toFind)
                element = element.NextNode;
            return element;
        }

        private CustomCollectionNode FindByIndex(ushort index)
        {
            var element = _firstItem;
            ushort counter = 0;
            while (element != null && counter != index)
            {
                element = element.NextNode;
                ++counter;
            }

            return element;
        }
    }
}