"""
estruturas condicionais 
if(se), else, elif (else = if)
"""
idade = 26
# if else em C
# if(idade<18){
#     printf("menor de idade");
# }else{
#   printf("maior de idade")


# }
# if else em Java
# if(idade<18){
#     System.out.println("menor de idade");
# }else{
#     System.out.println("maior de idade");
# }


if idade < 18:
    print('menor de idade')
elif idade ==18:
    print('Tem 18 anos')
else:
    print('maior de idade')   

# another way, but not indicated

if idade < 18:
    print('menor de idade')

if idade == 18:
    print('Tem 18 anos')

if idade > 18:
    print('é maior de idade')