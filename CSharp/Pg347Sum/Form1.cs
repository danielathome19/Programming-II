using Microsoft.VisualBasic;

namespace Pg347Sum {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            string variable = Interaction.InputBox("Prompt here", "Title");
            MessageBox.Show(variable);
        }
    }
}
