import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 327)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(226, 115)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(322, 327)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(226, 115)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(613, 327)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(226, 115)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 85)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(251, 53)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter Text:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 198)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(265, 77)
		self._label2.TabIndex = 4
		self._label2.Text = "Duplicates:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(322, 198)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(517, 77)
		self._label3.TabIndex = 5
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(322, 82)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(517, 53)
		self._textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(851, 496)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "StrInt1"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		myStr = self._textBox1.Text
		for lcv in range(len(myStr)):
			for lcv2 in range(lcv + 1, len(myStr)):
				letter1 = myStr[lcv]
				letter2 = myStr[lcv2]
				if letter1 == letter2:
					self._label3.Text += letter2 + " "
				
				