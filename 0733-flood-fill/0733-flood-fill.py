class Solution:
    def fill(self, image, sr, sc, color, curr):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return
        if curr != image[sr][sc]: return

        image[sr][sc] = color

        self.fill(image, sr-1, sc, color, curr)
        self.fill(image, sr+1, sc, color, curr)
        self.fill(image, sr, sc-1, color, curr)
        self.fill(image, sr, sc+1, color, curr)

    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color: return image
        self.fill(image, sr, sc, color, image[sr][sc])
        return image