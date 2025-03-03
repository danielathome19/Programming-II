import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(12, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(239, 48)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(385, 12)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(239, 48)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.WhiteSmoke
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 89)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(612, 176)
        self._label1.TabIndex = 2
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 277)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(184, 83)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(227, 277)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(184, 83)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(440, 277)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(184, 83)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self.ClientSize = System.Drawing.Size(636, 378)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "LP37"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        from DivAndMod import *
        dm1 = DivAndMod(num1, num2)
        dm2 = DivAndMod(num2, num1)
        dm1.calc()
        dm2.calc()
        div1 = dm1.get_div()
        mod1 = dm1.get_mod()
        div2, mod2 = dm2.get_divmod()
        self._label1.Text =  str(num1) + "/" + str(num2) + "=" + str(div1) + "\n"
        self._label1.Text += str(num1) + "%" + str(num2) + "=" + str(mod1) + "\n\n"
        self._label1.Text += str(num2) + "/" + str(num1) + "=" + str(div2) + "\n"
        self._label1.Text += str(num2) + "%" + str(num1) + "=" + str(mod2)
        pass