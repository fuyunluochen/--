#include <iostream>

using namespace std;
//�ַ��ͱ�������
char ch = 'A';

//�ַ��ͳ�������
//char ch2 = "c"; �����ַ��ͱ�����Ҫʹ�õ����š���;
//char ch3 = 'abcdefg';�ַ��ͱ�����������ֻ����1��


int main() {
    cout << ch << endl;
//    �ַ��ͱ���ռ���ڴ�
    cout << sizeof(ch) << "�ֽ�" << endl;
//�ַ��ͱ�����ӦASCII����
    cout << int(ch) << endl;
    system("pause");
    return 0;
}