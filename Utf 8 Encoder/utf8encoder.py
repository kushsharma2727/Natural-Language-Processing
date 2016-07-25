import sys

f = open(sys.argv[1], "rb")
x=bytearray()
try:
    byte = f.read(2)
    while byte != "":
                    #print byte
                    #print ord(byte[0])
                    #print ord(byte[1])
                    value=256*ord(byte[0]) + ord(byte[1])
                    
                    if value<=0x007F:
                        mask2=0b01111111
                        k1=mask2 & value
                        res=k1
                        #print "1"
                        #print res
                        x.append(res)
                        

                    elif(value<=0x07FF):
                        mask1=0b00111111
                        k1=mask1 & value #last 6 bits
                        v1=k1 | 0b10000000
                        mask2=0b11111000000
                        k2=mask2 & value #first 5 bits
                        k2=k2<<2
                        v2=k2 | 0b1100000000000000
                        res= v2 | v1
                        #print "2"
                        #print res
                        res1=0b11111111 & (res >> 8)
                        x.append(res1)
                        res2=0b11111111 & (res)
                        x.append(res2)
                        

                    elif(value>0x07FF):
                        mask1=0b00111111
                        k1=mask1 & value #last 6 bits
                        v1=k1 | 0b10000000
                        mask2=0b111111000000
                        k2=mask2 & value #next 6 bits
                        k2=k2<<2
                        v2=k2 | 0b1000000000000000
                        mask3=0b1111000000000000
                        k3=mask3 & value #first 4 bits
                        k3=k3<<4
                        v3=k3 | 0b111000000000000000000000
                        res1 = v3 | v2
                        res = res1 | v1
                        #print "3"
                        #print res
                        res1=0b11111111 & (res >> 16)
                        x.append(res1)
                        res2=0b11111111 & (res >> 8)
                        x.append(res2)
                        res3=0b11111111 & res
                        x.append(res3)
                        

                    
                    byte = f.read(2)
    out_file = open("utf8encoder_out.txt", "wb")
    out_file.write(x)
    out_file.close()
        
finally:
    f.close()

