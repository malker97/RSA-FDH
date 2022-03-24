#### 这是中间人的文件夹
生成两个Ciphertext来表示中间人已经拦截到的消息

#### 攻击一

##### TextMessage1

plaintext: `ItsBob`

Ciphertext:`GsCeSaUtweA07I7cUUKxJ22TB3+hQWaS72lSChEie7csPigioCmeKJ5CmeDsjWzgRtcuP3zm9l63w4QFQ/62pzICEgTiZJ0Cdf9OmTj7esTcBDJAojtHxwl0oWjD4HyzMU+a17GsjAdDbNDi9hMLdTPUJHFOVNRljNqAdZag9nk=`

Signature: 

```
)\xa4\xf6/\x85\x1c\x91x\xd8\x93T\x96c>\xa8\xedM*4\xad\xb5\xae8/6\x84\xd1\xc9\xdcYy\xad\xe1d\xadZQ\xcd\xa6\xe3^\x97C8)qG/\xf8\x81\xe1\xf3\xa0^\xe2\xd6\xb0\x0b\xf7\xb6u\xaa\xe9\xa2\x07\xbe\xb2\xe6\x8d\x13p\xb7\xfcZ\xed\xde\t\xb6\x90\xc00\xcc\x8d\xe8w\xadw((\xbf4\x1f\x9e\xa4GAu\xab-\xae6A\x83\x12 \x04\xa2\x9b~\xb8\x00q\xc9\x86R\x02\xfdn\xc0\x93\x1d\xa6_\x0e\xb4\xf5z\x92
```



##### TextMessage2

plaintext: `NGLITSREALBOB`

Ciphertext:`Qbi9R2AjTa07/G1Xna6rgI6VD/NrToI6O43nA2kEq1SyYeDF6/G2U04jvqZINk1nl/9AD7oGBIGjkRtTmYDwyMRTkSMg9JO9CByrJhel4WgLRJWipjEiihIe3Pl+QQGUuI16n+Hu84BxLfh7zd49HdtboFRP27Q2y2NPquzt1gM=`

Signature: 

```
D\x0f\x91k\xa3<8\xec\xa1\xaeT\x1fE\x88\x99\x14\xd3\xf5\xe2s\xb7@\xe6\xde\x91\xf9\xd0j\xad\xe4\xfb\x88\r\xe9\x92?\x8b\xd0\xc3\x024\x93\xe7\xd6\xaf'\x17\x82\xfb\x17]m[\x9cU\xa0s90\xd5O\xd3\xc5AlhY\x84)!\xf1\xd0$\xe8\xaa\x82\t\xce\xd3\xb1\x8f\xfa\xe8\n\x10\xcb\x8d\xb1\xdf^C\xab6\xd2\x9dl\xd5\x9f\x15.\xe8^>(;@\xa7\xc8`f\x11\t\x8a\x02\xf3R1\xd9\x8e@8\x87\x94Ex\xbcb/
```



##### 如果中间人想发起一次攻击，最容易的方法是发送一段秘闻，秘闻的内容转换为明文的时候为`ItsBobNGLITSREALBOB`或者是`NGLITSREALBOBItsBob`

##### 那么Alice是可以解密的，但是她声称的签名却不是$\delta_1 \times \delta_2$，因为这个Hash函数是单向的，并且不是映射的两个密码相加，此时验证签名就不能通过

声称fakesign的过程

```python
sign1 = fdh(b'ItsBob', 600)
sign2 = fdh(b'NGLITSREALBOB', 600)
sign1 = str.encode(sign1)
sign2 = str.encode(sign2)
sign1 =  int.from_bytes(sign1, "big", signed="True")
sign2 =  int.from_bytes(sign2, "big", signed="True")
print("ItsBob", sign1)
print("NGLITSREALBOB", sign2)
# print(sign1*sign2)
fake_sign = sign1 * sign2
fake_sign = str(fake_sign)
fake_sign = str.encode(fake_sign)
print(fake_sign)
```

我们生成的Fake_Sign为:

```
45119656720322030847730032154604610484765147099021474288956197326034794301610475678867932948350905424351575877982134903408334885057547344662103363331202829904186576287393178093741210680602998630482560036175983624459661560857427880704529583535644612093554742853762378002465881255666280619720347060186835352549830105302200324931227554781438413826928952366821122045251814931889517645161761773019427340434338005089449183180479972175425707940472837451543960384653335748530027575999972737379421904560213092036492846119601084671280880572170441149735142291703483807040644951450621712702024045804426217340174015580220204668966355274076617470174141800863962273721164009094440993803045415794146762964788547845637213002771530314162536401545193
```



#### 攻击二

如果是普通RSA加密的话，可以无数次模拟发送数字1，因为数字1的签名始终为1，即使之前没有拦截到，也可以尝试发送1



Reference: https://www.zhihu.com/question/27433132/answer/73474490
