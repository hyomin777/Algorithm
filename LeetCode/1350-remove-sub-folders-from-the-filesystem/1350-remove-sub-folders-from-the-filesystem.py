class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        dummy = sorted(folder)

        temp = ":"
        for i in range(len(dummy)):
            path = dummy[i]

            if path.startswith(temp):
                folder.remove(path)
            else:
                temp = path + "/"
        return folder