

def BinSearch(arr, numb) :
	arr.sort()
	print(arr)

	# 确定开始 结束为止
	iStart, iEnd, iPos = 0, len(arr), 0

	# 如果找到那么就退出
	while iStart < iEnd :
		iPos = int((iStart + iEnd) / 2);
		if arr[iPos] > numb :
			iEnd = iPos - 1
		elif arr[iPos] < numb :
			iStart = iPos + 1
		else :
			return iPos;
		print(iStart, iEnd, iPos)
		iPos = int((iStart + iEnd) / 2);

	return None, (iStart, iEnd) ;


if __name__ == '__main__':
	arr1 = [1, 3, 5, 2, 10, 7]
	print(BinSearch(arr1, 4))