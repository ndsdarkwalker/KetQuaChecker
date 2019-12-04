import requests
import bs4

resp = requests.get('http://ketqua.net')

tree = bs4.BeautifulSoup(resp.text, 'html.parser')
#DB
tree.find_all(attrs = {'id': 'rs_0_0'})
#1st
tree.find_all(attrs = {'id': 'rs_1_0'})
#2nd
tree.find_all(attrs = {'id': 'rs_2_0'})
tree.find_all(attrs = {'id': 'rs_2_1'})
#3rd
tree.find_all(attrs = {'id': 'rs_3_0'})
tree.find_all(attrs = {'id': 'rs_3_1'})
tree.find_all(attrs = {'id': 'rs_3_2'})
tree.find_all(attrs = {'id': 'rs_3_3'})
tree.find_all(attrs = {'id': 'rs_3_4'})
tree.find_all(attrs = {'id': 'rs_3_5'})
#4nd
tree.find_all(attrs = {'id': 'rs_4_0'})
tree.find_all(attrs = {'id': 'rs_4_1'})
tree.find_all(attrs = {'id': 'rs_4_2'})
tree.find_all(attrs = {'id': 'rs_4_3'})
#5nd
tree.find_all(attrs = {'id': 'rs_5_0'})
tree.find_all(attrs = {'id': 'rs_5_1'})
tree.find_all(attrs = {'id': 'rs_5_2'})
tree.find_all(attrs = {'id': 'rs_5_3'})
tree.find_all(attrs = {'id': 'rs_5_4'})
tree.find_all(attrs = {'id': 'rs_5_5'})
#6nd
tree.find_all(attrs = {'id': 'rs_6_0'})
tree.find_all(attrs = {'id': 'rs_6_1'})
tree.find_all(attrs = {'id': 'rs_6_2'})
#7nd
tree.find_all(attrs = {'id': 'rs_7_0'})
tree.find_all(attrs = {'id': 'rs_7_1'})
tree.find_all(attrs = {'id': 'rs_7_2'})
tree.find_all(attrs = {'id': 'rs_7_3'})

#DB
resultdb = tree.find_all(attrs = {'id': 'rs_0_0'})[0]
#1st
result1st = tree.find_all(attrs = {'id': 'rs_1_0'})[0]
#2nd
result2nd = tree.find_all(attrs = {'id': 'rs_2_0'})[0]
result2nd1 = tree.find_all(attrs = {'id': 'rs_2_1'})[0]
#3rd
result3rd = tree.find_all(attrs = {'id': 'rs_3_0'})[0]
result3rd1 = tree.find_all(attrs = {'id': 'rs_3_1'})[0]
result3rd2 = tree.find_all(attrs = {'id': 'rs_3_2'})[0]
result3rd3 = tree.find_all(attrs = {'id': 'rs_3_3'})[0]
result3rd4 = tree.find_all(attrs = {'id': 'rs_3_4'})[0]
result3rd5 = tree.find_all(attrs = {'id': 'rs_3_5'})[0]
#4nd
result4nd = tree.find_all(attrs = {'id': 'rs_4_0'})[0]
result4nd1 = tree.find_all(attrs = {'id': 'rs_4_1'})[0]
result4nd2 = tree.find_all(attrs = {'id': 'rs_4_2'})[0]
result4nd3 = tree.find_all(attrs = {'id': 'rs_4_3'})[0]
#5nd
result5nd = tree.find_all(attrs = {'id': 'rs_5_0'})[0]
result5nd1 = tree.find_all(attrs = {'id': 'rs_5_1'})[0]
result5nd2 = tree.find_all(attrs = {'id': 'rs_5_2'})[0]
result5nd3 = tree.find_all(attrs = {'id': 'rs_5_3'})[0]
result5nd4 = tree.find_all(attrs = {'id': 'rs_5_4'})[0]
result5nd5 = tree.find_all(attrs = {'id': 'rs_5_5'})[0]
#6nd
result6nd = tree.find_all(attrs = {'id': 'rs_6_0'})[0]
result6nd1 = tree.find_all(attrs = {'id': 'rs_6_1'})[0]
result6nd2 = tree.find_all(attrs = {'id': 'rs_6_2'})[0]
#7nd
result7nd = tree.find_all(attrs = {'id': 'rs_7_0'})[0]
result7nd1 = tree.find_all(attrs = {'id': 'rs_7_1'})[0]
result7nd2 = tree.find_all(attrs = {'id': 'rs_7_2'})[0]
result7nd3 = tree.find_all(attrs = {'id': 'rs_7_3'})[0]

print("\n")
print("MUA VÉ SỐ CHƯA MÀ DÒ RỐI !!!\n")

print("Giải đặc biệt: \n", resultdb.text)

print("Giải nhất: \n", result1st.text)

print("Giải nhì:\n", result2nd.text)
print('',result2nd1.text)

print("Giải ba:\n", result3rd.text)
print('',result3rd1.text)
print('',result3rd2.text)
print('',result3rd3.text)
print('',result3rd4.text)
print('',result3rd5.text)

print("Giải tư:\n", result4nd.text)
print('',result4nd1.text)
print('',result4nd2.text)
print('',result4nd3.text)

print("Giải năm:\n", result5nd.text)
print('',result5nd1.text)
print('',result5nd2.text)
print('',result5nd3.text)
print('',result5nd4.text)
print('',result5nd5.text)

print("Giải sáu:\n", result6nd.text)
print('',result6nd1.text)
print('',result6nd2.text)

print("Giải bảy:\n", result7nd.text)
print('',result7nd1.text)
print('',result7nd2.text)
print('',result7nd3.text)

print("TRÚNG CHƯA?")
