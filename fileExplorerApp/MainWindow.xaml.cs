using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows;
using System.Windows.Controls;

namespace FileExplorer
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            foreach (var dir in Directory.GetLogicalDrives())
            {
                // create a tree view item for each directory
                TreeViewItem dirItem = new TreeViewItem() { Header = dir, Tag = dir };

                dirItem.Expanded += Directory_Expanded;
                
                // add it to the tree view control
                treeviewList.Items.Add(dirItem);
            }

            
        }


        private void Directory_Expanded(object sender, RoutedEventArgs e)
        {
            TreeViewItem item = (TreeViewItem)sender;
            if (item.Items.Count == 0)
            {
                // this is the first time the directory item is being expanded
                // need to load the sub-directories
                var subDirectories = new List<string>();
                var allFiles = new List<string>();
                try
                {
                    string[] dirs = Directory.GetDirectories((string)item.Tag);
                    string[] files = Directory.GetFiles((string)item.Tag);
                    if (dirs.Length > 0)
                    {
                        subDirectories.AddRange(dirs);
                    }
                    if (files.Length > 0)
                    {
                        allFiles.AddRange(files);
                    }
                }
                
                // Something went wrong with getting subdirectories but we ignore it
                catch { }

                foreach (string subItem in subDirectories)
                {
                    TreeViewItem subTreeItem = new TreeViewItem() { Header = Path.GetFileName(subItem), Tag = subItem };
                    subTreeItem.Expanded += Directory_Expanded;
                    item.Items.Add(subTreeItem);
                }

                foreach (string subFile in allFiles)
                {
                    TreeViewItem subFileItem = new TreeViewItem() { Header = Path.GetFileName(subFile), Tag = subFile };
                    item.Items.Add(subFileItem);
                }


            }
            else
            {
                // don't need to load the sub-directories again
                return;
            }
        }
    }

}
