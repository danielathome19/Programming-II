import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkRed
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(319, 263)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(281, 97)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkRed
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(12, 263)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(281, 97)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(299, 9)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(302, 48)
        self._textBox1.TabIndex = 9
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(299, 170)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(302, 50)
        self._label3.TabIndex = 8
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightCoral
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 170)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(259, 50)
        self._label2.TabIndex = 7
        self._label2.Text = "Anagrams?"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightCoral
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(259, 48)
        self._label1.TabIndex = 6
        self._label1.Text = "Enter word1:"
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(299, 86)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(302, 48)
        self._textBox2.TabIndex = 13
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightCoral
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 86)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(259, 48)
        self._label4.TabIndex = 12
        self._label4.Text = "Enter word2:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self.ClientSize = System.Drawing.Size(612, 376)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StrInt2"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._label3.Text = ""
        word1 = self._textBox1.Text.lower()
        word2 = self._textBox2.Text.lower()
        # self._label3.Text = sorted(word1) == sorted(word2)
        
        if len(word1) != len(word2):
            self._label3.Text = "False"
            return
        else:
            for lcv in range(len(word1)):
                c = word1[lcv]
                index = word2.find(c)
                if index == -1:
                    self._label3.Text = "False"
                else:
                    word2 = word2[0:index] + word2[index+1:]
        self._label3.Text = str(len(word2) == 0)
        pass