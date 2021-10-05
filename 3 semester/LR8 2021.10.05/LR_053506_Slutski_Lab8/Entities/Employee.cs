namespace LR_053506_Slutski_Lab8.Entities
{
    public class Employee
    {
        public string Name { get; set; }

        public ushort Salary { get; set; }
        public bool Remote { get; set; }


        public Employee(string name, ushort salary, bool remote = false) =>
            (Name, Remote, Salary) = (name, remote, salary);

        public override string ToString() => $"{Name} {Salary} {Remote}";
    }
}