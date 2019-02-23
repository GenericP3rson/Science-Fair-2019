import wx


class Example(wx.Frame):

    i = "/Users/paromitadatta/Desktop/dukelogo.png"
    qqq = []

    def __init__(self, *args, **kwargs):
        super(Eçxample, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.panel = wx.Panel(self, wx.ID_ANY)

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        BlurringPicture = fileMenu.Append(wx.NewId(), "Blurring",
                                          "Blurs the picture")
        BrightenPicture = fileMenu.Append(wx.NewId(), "Brighten",
                                          "Brightens the picture")
        DarkenPicture = fileMenu.Append(wx.NewId(), "Darken",
                                        "Darkens the picture")
        GreyScalePicture = fileMenu.Append(wx.NewId(), "GreyScale",
                                           "Greys the picture")
        InvertPicture = fileMenu.Append(wx.NewId(), "Invert",
                                        "Inverts the picture")
        PosterizePicture = fileMenu.Append(wx.NewId(), "Posterize",
                                           "Posterizes the picture")
        SolarizePicture = fileMenu.Append(wx.NewId(), "Solarize",
                                          "Solarizes the picture")
        menuBar.Append(fileMenu, "&Filters")
        # iiii = 0
        # ii = [BlurringPicture, BrightenPicture, DarkenPicture, GreyScalePicture, InvertPicture, PosterizePicture, SolarizePicture]
        # iii = [self.Blur, self.Bright, self.Dark, self.Grey, self.UpsideDown, self.Post, self.Solar]
        # while (iiii < len(ii)):
        #     self.Bind(wx.EVT_MENU, iii[iiii], ii[iiii])
        #     iiii+=1
        # def Blur(event):
        #     from PIL import Image
        #     from PIL import ImageFilter
        #     original_image = i
        #     original_image = Image.open(original_image)
        #     blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=5))
        #     blurred_image.save("processedImage.png")
        #     blurred_image.show()
        self.Bind(wx.EVT_MENU, self.Blur, BlurringPicture)
        self.Bind(wx.EVT_MENU, self.Bright, BrightenPicture)
        self.Bind(wx.EVT_MENU, self.Dark, DarkenPicture)
        self.Bind(wx.EVT_MENU, self.Grey, GreyScalePicture)
        self.Bind(wx.EVT_MENU, self.UpsideDown, InvertPicture)
        self.Bind(wx.EVT_MENU, self.Post, PosterizePicture)
        self.Bind(wx.EVT_MENU, self.Solar, SolarizePicture)
        self.SetMenuBar(menuBar)

        #WILL OPEN THE IMAGE WITH THE CHOICES

        #NEW IMAGE

        # aweer = ["/Users/paromitadatta/Desktop/Folder3/Folder3.2/Folder3.23/processed_image.png", "/Users/paromitadatta/Desktop/Folder3/Folder3.2/Folder3.23/processed_image.png"]
        # awe = 0
        # while (awe < 2):
        import os
        # import wx

        class PhotoCtrl(wx.App):
            i = ""

            def __init__(self, redirect=False, filename=None):
                wx.App.__init__(self, redirect, filename)
                self.frame = wx.Frame(None, title='Photo Control')

                self.panel = wx.Panel(self.frame)

                self.PhotoMaxSize = 240

                self.createWidgets()
                self.frame.Show()
                # self.i = self.ret()
                # print(self.i)
                # print("YYYYYYYYY")

            def createWidgets(self):
                instructions = 'Browse for an image'
                img = wx.EmptyImage(240, 240)
                self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                                 wx.BitmapFromImage(img))

                instructLbl = wx.StaticText(self.panel, label=instructions)
                self.photoTxt = wx.TextCtrl(self.panel, size=(200, -1))
                browseBtn = wx.Button(self.panel, label='Browse')
                browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

                self.mainSizer = wx.BoxSizer(wx.VERTICAL)
                self.sizer = wx.BoxSizer(wx.HORIZONTAL)

                self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                                   0, wx.ALL | wx.EXPAND, 5)
                self.mainSizer.Add(instructLbl, 0, wx.ALL, 5)
                self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
                self.sizer.Add(self.photoTxt, 0, wx.ALL, 5)
                self.sizer.Add(browseBtn, 0, wx.ALL, 5)
                self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)

                self.panel.SetSizer(self.mainSizer)
                self.mainSizer.Fit(self.frame)

                self.panel.Layout()

            def onBrowse(self, event):
                """
                Browse for file
                """
                app = wx.App(False)
                frame = wx.Frame(None, -1, 'PhotoShop')
                frame.SetDimensions(0, 0, 200, 50)
                # Create open file dialog
                openFileDialog = wx.FileDialog(frame, "Open", "", "",
                                               "PNG files (*.png)|*.png",
                                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

                openFileDialog.ShowModal()
                print(openFileDialog.GetPath())
                self.i = str(openFileDialog.GetPath())
                from PIL import Image
                img = Image.open(self.i)
                # img.show()
                wildcard = "JPEG files (*.jpg)|*.jpg"
                dialog = self.i
                #if dialog.ShowModal() == wx.ID_OK:
                self.photoTxt.SetValue(dialog)
                #dialog.Destroy()
                self.i = self.ret
                print("@@@@@@@@@@@@@@@@@@@@")
                print(self.i)
                print("@@@@@@@@@@@@@@@@@@@@")
                self.onView()
                self.onView1()

            def ret(self):
                return self.photoTxt.GetValue()

            def onView(self):
                filepath = self.photoTxt.GetValue()
                img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
                # scale the image, preserving the aspect ratio
                W = img.GetWidth()
                H = img.GetHeight()
                if W > H:
                    NewW = self.PhotoMaxSize
                    NewH = self.PhotoMaxSize * H / W
                else:
                    NewH = self.PhotoMaxSize
                    NewW = self.PhotoMaxSize * W / H
                img = img.Scale(NewW, NewH)

                self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
                self.panel.Refresh()

            def onView1(self):
                filepath = self.photoTxt.GetValue()
                img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
                # scale the image, preserving the aspect ratio
                W = img.GetWidth()
                H = img.GetHeight()
                if W > H:
                    NewW = self.PhotoMaxSize
                    NewH = self.PhotoMaxSize * H / W
                else:
                    NewH = self.PhotoMaxSize
                    NewW = self.PhotoMaxSize * W / H
                img = img.Scale(NewW, NewH)

                self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
                self.panel.Refresh()

        if __name__ == '__main__':
            app = PhotoCtrl()
            self.i = app.ret()
            print(self.i)
            print("HOOOOOOOOOOOOOOOPPPPEEEEEE")
            app.MainLoop()
        # awe+=1

        # menubar = wx.MenuBar()
        # fileMenu = wx.Menu()
        # fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        # menubar.Append(fileMenu, '&File')
        # self.SetMenuBar(menubar)

        # self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        # self.SetSize((300, 200))
        # self.SetTitle('Simple menu')
        # self.Centre()
    # i = "/Users/paromitadatta/Desktop/dukelogo.png"

    def onExit(self, e):
        self.Close()

    def Blur(self, event):
        try:
            i = self.i
            print(i)
            print("@@$(@#)$#(!$!#)@$*@#")
            from PIL import Image
            from PIL import ImageFilter
            original_image = self.i
            original_image = Image.open(original_image)
            blurred_image = original_image.filter(
                ImageFilter.GaussianBlur(radius=5))
            blurred_image.save("processedImage.png")
            blurred_image.show()
        except:
            print("There's been an error using your image. Enjoy this for now!")
            from PIL import Image
            from PIL import ImageFilter
            original_image = "/Users/paromitadatta/Desktop/Jaguar-PNG-Image-18102.png"
            original_image = Image.open(original_image)
            blurred_image = original_image.filter(
                ImageFilter.GaussianBlur(radius=5))
            blurred_image.save("processedImage.png")
            blurred_image.show()

        # blurImage(i)

    def Bright(self, event):
        try:
            i = self.i
            from PIL import Image
            img = Image.open(i)
            pixels = [(int(r * 1.25), int(g * 1.25), int(b * 1.25))
                      for (r, g, b, a) in img.getdata()]
            img.putdata(pixels)
            img.save("processedImage.png")
            img.show()
        except:
            i = "/Users/paromitadatta/Desktop/Jaguar-PNG-Image-18102.png"
            from PIL import Image
            img = Image.open(i)
            pixels = [(int(r * 1.25), int(g * 1.25), int(b * 1.25))
                      for (r, g, b, a) in img.getdata()]
            img.putdata(pixels)
            img.save("processedImage.png")
            img.show()

    def Dark(self, event):
        try:
            i = self.i
            from PIL import Image
            img = Image.open(i)
            pixels = [(int(r * .75), int(g * .75), int(b * .75))
                      for (r, g, b, a) in img.getdata()]
            img.putdata(pixels)
            img.save("processedImage.png")
            img.show()
        except:
            i = "/Users/paromitadatta/Desktop/Jaguar-PNG-Image-18102.png"
            from PIL import Image
            img = Image.open(i)
            pixels = [(int(r * .75), int(g * .75), int(b * .75))
                      for (r, g, b, a) in img.getdata()]
            img.putdata(pixels)
            img.save("processedImage.png")
            img.show()

    def Grey(self, event):
        try:
            i = self.i
            from PIL import Image
            img = Image.open(i)
        except:
            i = "/Users/paromitadatta/Desktop/Jaguar-PNG-Image-18102.png"
            from PIL import Image
            img = Image.open(i)
        pixels = [(int(r), int(g), int(b)) for (r, g, b, a) in img.getdata()]
        new_pixels = []
        for (r, g, b) in pixels:
            grey = int((r+g+b)/3.0)
            new_pixel = (grey, grey, grey)
            new_pixels.append(new_pixel)
        img.putdata(new_pixels)
        img.save("processedImage.png")
        img.show()

    def UpsideDown(self, event):
        try:
            i = self.i
            from PIL import Image
            img = Image.open(i)
        except:
            i = "/Users/paromitadatta/Desktop/Jaguar-PNG-Image-18102.png"
            from PIL import Image
            img = Image.open(i)

        # img = Image.open(i)
        pixels = [(int(255 - r), int(255 - g), int(255 - b))
                  for (r, g, b, a) in img.getdata()]
        img.putdata(pixels)
        img.save("processedImage.png")
        img.show()

    def Post(self, event):
        try:
            i = self.i
            from PIL import Image
            img = Image.open(i)
        except:
            i = "/Users/paromitadatta/Desktop/Jaguar-PNG-Image-18102.png"
            from PIL import Image
            img = Image.open(i)

        pixels = [(int(r), int(g), int(b), int(a))
                  for (r, g, b, a) in img.getdata()]
        new_pixels = []
        for (r, g, b, a) in pixels:
            if r >= 0 and r <= 63:
                great = 50
            elif r >= 64 and r <= 127:
                great = 100
            elif r >= 128 and r <= 191:
                great = 150
            elif r >= 192 and r <= 255:
                great = 200

            if g >= 0 and g <= 63:
                brown = 50
            elif g >= 64 and g <= 127:
                brown = 100
            elif g >= 128 and g <= 191:
                brown = 150
            elif g >= 192 and g <= 255:
                brown = 200

            if b >= 0 and b <= 63:
                um = 50
            elif b >= 64 and b <= 127:
                um = 100
            elif b >= 128 and b <= 191:
                um = 150
            elif b >= 192 and b <= 255:
                um = 200
            new_pixel = (great, brown, um)
            new_pixels.append(new_pixel)
        img.putdata(new_pixels)
        img.save("processedImage.png")
        img.show()

    def Solar(self, event):
        try:
            i = self.i
            from PIL import Image
            img = Image.open(i)
        except:
            i = "/Users/paromitadatta/Desktop/Jaguar-PNG-Image-18102.png"
            from PIL import Image
            img = Image.open(i)

        img = Image.open(i)
        pixels = [(int(r), int(g), int(b)) for (r, g, b, a) in img.getdata()]
        new_pixel = []
        for (r, g, b) in pixels:
            if r < 128:
                r = 255 - r
            if g < 128:
                g = 255 - g
            if b < 128:
                b = 255 - b
            new_pixels = (r, g, b)
            new_pixel.append(new_pixels)
        img.putdata(new_pixel)
        img.save("processedImage.png")
        img.show()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()