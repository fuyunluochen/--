#include <iostream>
#include <windows.h>

void reavelPath(char *pathName) {
	char fileName[MAX_PATH] = {0};
	sprintf(fileName, "%s\\*.*", pathName);
	WIN32_FIND_DATA findData = {0};
//	printf("文件名是：%s\n", fileName);
	HANDLE hfile = FindFirstFile(fileName, &findData);
	if (INVALID_HANDLE_VALUE == hfile) {
		printf("第一个文件就失败了");
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
				printf("文件夹---：%s\n", temp);
				reavelPath(temp);
			}
		} else {
			printf("文件:%s\n", temp);

		}
	}
}

int main() {

	char buff[MAX_PATH];
	GetCurrentDirectory(MAX_PATH, buff);
//	printf("当前文件夹:%s\n", buff);
	reavelPath(buff);
	return 0;
}