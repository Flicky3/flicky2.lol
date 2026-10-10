Add-Type -AssemblyName System.Drawing
$srcPath = "C:\Users\Flicky\.gemini\antigravity\brain\390e2183-0fa5-4c0f-9d29-adb279e195bf\.user_uploaded\media_1791617160236_ac01fd2e.png"
$dstPath = "C:\Users\Flicky\.gemini\antigravity\scratch\guns-profile\pfp.png"

$img = [System.Drawing.Image]::FromFile($srcPath)

# Inner photo inside the black circular border:
$cropX = 49
$cropY = 85
$cropSize = 82

$cropRect = New-Object System.Drawing.Rectangle($cropX, $cropY, $cropSize, $cropSize)
$bmp = New-Object System.Drawing.Bitmap($cropSize, $cropSize)
$graphics = [System.Drawing.Graphics]::FromImage($bmp)
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$destRect = New-Object System.Drawing.Rectangle(0, 0, $cropSize, $cropSize)

$graphics.DrawImage($img, $destRect, $cropRect, [System.Drawing.GraphicsUnit]::Pixel)

$graphics.Dispose()
$img.Dispose()

$bmp.Save($dstPath, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Write-Host "Inner PFP photo cropped perfectly!"
