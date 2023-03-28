using MaterialDesignThemes.Wpf;
using System;
using System.Globalization;
using System.IO;
using System.Windows;
using System.Windows.Data;

namespace FileExplorer
{
    [ValueConversion(typeof(string), typeof(PackIconKind))]
    class HeaderToPackIconKindConverter : IValueConverter
    {
        public static HeaderToPackIconKindConverter Instance = new HeaderToPackIconKindConverter();
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            string filePath = (string)value;
            
            if (filePath == null)
            { return null; }


            //detect whether its a directory or file
            FileAttributes attr = File.GetAttributes(filePath);

            // TODO: Display different icons for collapsed and uncollapsed items
            if ((attr & FileAttributes.Directory) == FileAttributes.Directory)
                return PackIconKind.Folder;
            else
                return PackIconKind.FileDocumentOutline;
        }
        public object ConvertBack(object value, Type type, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
