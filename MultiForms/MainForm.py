import System.Drawing
import System.Windows.Forms
# import Form1
# form1 = Form1.Form1()
# from Form1 import Form1

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(72, 58)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(568, 419)
		self._button1.TabIndex = 0
		self._button1.Text = "Show New Form"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Red
		self.ClientSize = System.Drawing.Size(689, 553)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MultiForms"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Hello, world!")
		form1.Show()
		self.Hide()
		
		# from SecondForm import *
		# form2 = SecondForm()
		# form2.Show()