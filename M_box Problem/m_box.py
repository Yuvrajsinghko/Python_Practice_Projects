m_box_file=open('mbox.txt','r')
m_box_data=m_box_file.readlines()
m_box_file.close()
print(type(m_box_data))
for i in m_box_data:
	print(i)
