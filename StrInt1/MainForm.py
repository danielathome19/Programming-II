import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Cyan
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(259, 48)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter text:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Cyan
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 119)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(259, 50)
        self._label2.TabIndex = 1
        self._label2.Text = "Duplicates:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(299, 119)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(302, 50)
        self._label3.TabIndex = 2
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(299, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(302, 48)
        self._textBox1.TabIndex = 3
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
        self._button1.Location = System.Drawing.Point(12, 212)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(235, 97)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
        self._button2.Location = System.Drawing.Point(366, 212)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(235, 97)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self.ClientSize = System.Drawing.Size(613, 321)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StrInt1"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._label3.Text = ""
        myStr = self._textBox1.Text.lower()
        for lcv in range(len(myStr)):
            for lcv2 in range(lcv+1, len(myStr)):
                ltr1 = myStr[lcv]
                ltr2 = myStr[lcv2]
                if ltr1 == ltr2:
                    self._label3.Text += ltr2 + " "
        pass

    def Button2Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = ""