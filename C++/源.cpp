#include <iostream>
#include <windows.h>

void reavelPath(char *pathName) {
	char fileName[MAX_PATH] = {0};
	sprintf(fileName, "%s\\*.*", pathName);
	WIN32_FIND_DATA findData = {0};
//	printf("�ļ����ǣ�%s\n", fileName);
	HANDLE hfile = FindFirstFile(fileName, &findData);
	if (INVALID_HANDLE_VALUE == hfile) {
		printf("��һ���ļ���ʧ����");
		return;
	}
	char temp[MAX_PATH];
	BOOL ret = true;
	while (ret) {
		memset(temp, 0, MAX_PATH);
		sprintf(temp, "%s\\%s", pathName, findData.cFileName);
		ret = FindNextFile(hfile, &findData);
		if (FILE_ATTRIBUTE_DIRECTORY == findData.dwFileAttributes) {
			if ('.' != findData.cFileName[0]) {
				printf("�ļ���---��%s\n", temp);
				reavelPath(temp);
			}
		} else {
			printf("�ļ�:%s\n", temp);

		}
	}
}

int main() {

	char buff[MAX_PATH];
	GetCurrentDirectory(MAX_PATH, buff);
//	printf("��ǰ�ļ���:%s\n", buff);
	reavelPath(buff);
	return 0;
}