using Microsoft.VisualBasic;

namespace Pg498Payroll {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        const int intMAX_EMPLOYEES = 5;
        const decimal decHOURLY_PAY_RATE = 6.0m;
        private void button1_Click(object sender, EventArgs e) {
            // Calc & Display Gross Pay Earned by Employees
            int[] intHours = new int[intMAX_EMPLOYEES];  // An array [0,0,0,0,0]
            // <type>[] varName = new <type>[capacity];
            int Count = 0;
            int EmpHours = 0;
            decimal EmpPay = 0.0m;

            for (Count = 0; Count < intMAX_EMPLOYEES; Count++) {
                while (int.TryParse(
                     Interaction.InputBox("Enter # of hours worked by employee #" +
                     (Count+1).ToString(), "Need Hours Worked"), 
                     out EmpHours) == false) {
                    MessageBox.Show("Please enter an integer for hours worked");
                }
                intHours[Count] = EmpHours;
            }

            // TODO: the rest
        }
    }
}
