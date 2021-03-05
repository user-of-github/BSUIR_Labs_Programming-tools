using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;

namespace LR1_2021._02._15
{
    internal static class Program
    {
        private static void Main() => GameMenu.Launch();
    }

    static class Labyrinth
    {
        private struct Position
        {
            public sbyte Row, Col;
        }

        private static readonly sbyte[,] Directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        private static sbyte _marginLeftSize, _marginTopSize;
        private static string _marginLeft, _marginTop;

        private const string Texture = "██", FreeSpace = "  ";

        private const ConsoleColor DefaultConsoleFontColor = ConsoleColor.White,
            ColorPlayer = ConsoleColor.DarkGreen,
            ColorAutoPassHead = ConsoleColor.DarkRed,
            ColorAutoPassBody = ConsoleColor.Green;

        private const string MessageSuccess = "PASSED SUCCESSFULLY",
            MessageFail = "FAILED TO PASS";

        private const byte TimingDelayBFS = 30,
            TimingDelayDFSIn = 35,
            TimingDelayDFSOut = 7,
            TimingDelayPrintingField = 3;

        private static byte _width, _height;
        private static readonly List<List<bool>> Field = new List<List<bool>>();

        private static Position _startCoordinate, _finishCoordinate;

        public static void LoadLabyrinth(ref string filePath)
        {
            Field.Clear();
            Console.CursorVisible = false;
            var lines = File.ReadAllLines(filePath);
            _height = Convert.ToByte(lines[0].Split(' ')[0]);
            _width = Convert.ToByte(lines[0].Split(' ')[1]);
            for (sbyte counter = 1; counter < _height + 1; ++counter)
            {
                var tempRowList = lines[counter].Select(state => state != '█').ToList();
                Field.Add(tempRowList);
            }

            _startCoordinate = new Position
            {
                Row = (sbyte) (sbyte.Parse(lines[^2].Split(' ')[0]) - 1),
                Col = (sbyte) (sbyte.Parse(lines[^2].Split(' ')[1]) - 1)
            };

            _finishCoordinate = new Position
            {
                Row = (sbyte) (sbyte.Parse(lines[^1].Split(' ')[0]) - 1),
                Col = (sbyte) (sbyte.Parse(lines[^1].Split(' ')[1]) - 1)
            };

            _marginLeftSize = (sbyte) (Console.WindowWidth / 2 - _width - 1);
            _marginTopSize = (sbyte) (Console.WindowHeight / 2 - _height / 2 - 1);
            _marginLeft = new string(' ', _marginLeftSize);
            _marginTop = new string('\n', _marginTopSize);
        }

        private static void PrintField()
        {
            Console.OutputEncoding = Encoding.UTF8;

            Console.Write(_marginTop);
            Console.ForegroundColor = DefaultConsoleFontColor;
            foreach (var row in Field)
            {
                Console.Write(_marginLeft);
                foreach (var state in row) Console.Write(state ? "  " : Texture);
                Console.Write('\n');
                Thread.Sleep(TimingDelayPrintingField);
            }

            Console.Write('\n');
        }

        private static void PrintByCoordinate(sbyte y, sbyte x, string info)
        {
            Console.SetCursorPosition(x, y);
            Console.Write(info);
        }

        private static void SearchInLabirint(ref bool foundPath, ref int[,] visitedPositions, bool toPrint)
        {
            var visitedCells = new Queue<Position>();

            visitedCells.Enqueue(_startCoordinate);

            while (visitedCells.Count > 0 && !foundPath)
            {
                var currentPosition = visitedCells.Dequeue();
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (sbyte) (currentPosition.Col + Directions[counter, 0]);
                    var y = (sbyte) (currentPosition.Row + Directions[counter, 1]);


                    if (x >= 0 && x < _width && y >= 0 && y < _height && visitedPositions[y, x] == 0 &&
                        !(x == _startCoordinate.Col && y == _startCoordinate.Row))
                    {
                        if (toPrint)
                        {
                            Console.ForegroundColor = ColorAutoPassBody;
                            PrintByCoordinate((sbyte) (_marginTopSize + y), (sbyte) (x * 2 + _marginLeftSize), Texture);
                            Thread.Sleep(TimingDelayDFSIn);
                        }

                        visitedPositions[y, x] = visitedPositions[currentPosition.Row, currentPosition.Col] + 1;
                        visitedCells.Enqueue(new Position {Row = y, Col = x});
                    }

                    if (y == _finishCoordinate.Row && x == _finishCoordinate.Col)
                    {
                        foundPath = true;
                        break;
                    }
                }
            }
        }

        private static IEnumerable<Position> GetPath(ref int[,] visitedPositions)
        {
            var path = new Position[visitedPositions[_finishCoordinate.Row, _finishCoordinate.Col] + 1];
            int pathIndex = 0;
            path[pathIndex] = _finishCoordinate;

            while (!(path[pathIndex].Row == _startCoordinate.Row &&
                     path[pathIndex].Col == _startCoordinate.Col))
            {
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (SByte) (path[pathIndex].Col + Directions[counter, 0]);
                    var y = (SByte) (path[pathIndex].Row + Directions[counter, 1]);

                    if (x >= 0 && x < _width && y >= 0 && y < _height && visitedPositions[y, x] != -1 &&
                        visitedPositions[y, x] == visitedPositions[path[pathIndex].Row, path[pathIndex].Col] - 1)
                    {
                        path[++pathIndex] = (new Position {Row = y, Col = x});
                        break;
                    }
                }
            }

            return path;
        }

        private static void ShowPassage(ref Position[] path)
        {
            var previousCoordinate = _startCoordinate;
            foreach (var currentCoordinate in path)
            {
                Console.ForegroundColor = ColorAutoPassBody;
                PrintByCoordinate((sbyte) (previousCoordinate.Row + _marginTopSize),
                    (sbyte) (previousCoordinate.Col * 2 + _marginLeftSize), Texture);

                previousCoordinate = currentCoordinate;
                Console.ForegroundColor = ColorAutoPassHead;

                PrintByCoordinate((sbyte) (currentCoordinate.Row + _marginTopSize),
                    (sbyte) (currentCoordinate.Col * 2 + _marginLeftSize), Texture);

                Thread.Sleep(TimingDelayBFS);
            }

            Console.ForegroundColor = DefaultConsoleFontColor;
        }

        public static void PassByComputerBFS()
        {
            var visitedPositions = new int[_height, _width];
            for (sbyte row = 0; row < _height; ++row)
            for (sbyte col = 0; col < _width; ++col)
                visitedPositions[row, col] = (Field[row][col] ? 0 : -1);

            visitedPositions[_startCoordinate.Row, _startCoordinate.Col] = 0;

            var foundPath = false;

            SearchInLabirint(ref foundPath, ref visitedPositions, false);

            PrintField();
            if (foundPath)
            {
                var path = GetPath(ref visitedPositions).Reverse().ToArray();
                ShowPassage(ref path);
            }

            PrintByCoordinate((sbyte) (_height + _marginTopSize + 1), _marginLeftSize,
                (foundPath ? MessageSuccess : MessageFail));
            Console.Write($"\n\n{_marginLeft}");
        }

        private static void DFS(Position currentPosition, ref bool[,] visitedPositions, ref bool foundPath)
        {
            visitedPositions[currentPosition.Row, currentPosition.Col] = true;
            if (currentPosition.Row == _finishCoordinate.Row && currentPosition.Col == _finishCoordinate.Col)
            {
                foundPath = true;
                return;
            }

            for (sbyte counter = 0; counter < 4; ++counter)
            {
                var x = (sbyte) (currentPosition.Col + Directions[counter, 0]);
                var y = (sbyte) (currentPosition.Row + Directions[counter, 1]);

                if (x >= 0 && x < _width && y >= 0 && y < _height && Field[y][x] &&
                    !visitedPositions[y, x])
                {
                    PrintByCoordinate((sbyte) (y + _marginTopSize), (sbyte) (x * 2 + _marginLeftSize), Texture);
                    Thread.Sleep(TimingDelayDFSIn);
                    DFS(new Position {Row = y, Col = x}, ref visitedPositions, ref foundPath);
                    Thread.Sleep(TimingDelayDFSOut);
                    PrintByCoordinate((sbyte) (y + _marginTopSize), (sbyte) (x * 2 + _marginLeftSize), FreeSpace);
                }
            }
        }

        public static void VisualizePassingByComputerWithDFS()
        {
            PrintField();

            var foundPath = false;
            var visitedPositions = new bool [_height, _width];
            for (sbyte row = 0; row < _height; ++row)
            for (sbyte col = 0; col < _width; ++col)
                visitedPositions[row, col] = !Field[row][col];

            Console.ForegroundColor = ColorAutoPassBody;
            PrintByCoordinate((sbyte) (_startCoordinate.Row + _marginTopSize),
                (sbyte) (_startCoordinate.Col * 2 + _marginLeftSize), Texture);
            DFS(_startCoordinate, ref visitedPositions, ref foundPath);

            Console.ForegroundColor = DefaultConsoleFontColor;
            PrintByCoordinate((sbyte) (_height + _marginTopSize + 1), _marginLeftSize,
                (foundPath ? MessageSuccess : MessageFail));
            Console.Write($"\n\n{_marginLeft}");
        }

        public static void VisualizePassingByComputerWithBFS()
        {
            PrintField();
            var visitedPositions = new int[_height, _width];
            for (sbyte row = 0; row < _height; ++row)
            for (sbyte col = 0; col < _width; ++col)
                visitedPositions[row, col] = (Field[row][col] ? 0 : -1);

            visitedPositions[_startCoordinate.Row, _startCoordinate.Col] = 0;

            var foundPath = false;

            SearchInLabirint(ref foundPath, ref visitedPositions, true);

            Console.ForegroundColor = DefaultConsoleFontColor;
            PrintByCoordinate((sbyte) (_height + _marginTopSize + 1), _marginLeftSize,
                (foundPath ? MessageSuccess : MessageFail));
            Console.Write($"\n\n{_marginLeft}");
        }

        private static void MovePlayer(ref Position previous, ref Position current)
        {
            PrintByCoordinate((sbyte) (previous.Row + _marginTopSize), (sbyte) (previous.Col * 2 + _marginLeftSize),
                FreeSpace);
            PrintByCoordinate((sbyte) (current.Row + _marginTopSize), (sbyte) (current.Col * 2 + _marginLeftSize),
                Texture);
        }

        private static bool ComputeKeyPressed(ref ConsoleKeyInfo keyPressed, ref Position player)
        {
            switch (keyPressed.Key)
            {
                case ConsoleKey.UpArrow:
                {
                    if (player.Row >= 1 && Field[player.Row - 1][player.Col])
                    {
                        --player.Row;
                        return true;
                    }

                    break;
                }
                case ConsoleKey.DownArrow:
                {
                    if (player.Row + 1 < _height && Field[player.Row + 1][player.Col])
                    {
                        ++player.Row;
                        return true;
                    }

                    break;
                }
                case ConsoleKey.LeftArrow:
                {
                    if (player.Col >= 1 && Field[player.Row][player.Col - 1])
                    {
                        --player.Col;
                        return true;
                    }

                    break;
                }
                case ConsoleKey.RightArrow:
                {
                    if (player.Col + 1 < _width && Field[player.Row][player.Col + 1])
                    {
                        ++player.Col;
                        return true;
                    }

                    break;
                }
            }

            return false;
        }

        public static void Play()
        {
            var isWinner = false;
            var playerPosition = _startCoordinate;
            ConsoleKeyInfo keyPressed;

            PrintField();

            Console.ForegroundColor = ColorPlayer;
            PrintByCoordinate((sbyte) (playerPosition.Row + _marginTopSize),
                (sbyte) (playerPosition.Col * 2 + _marginLeftSize), Texture);
            do
            {
                keyPressed = Console.ReadKey(true);
                var previousPosition = playerPosition;

                if (ComputeKeyPressed(ref keyPressed, ref playerPosition))
                    MovePlayer(ref previousPosition, ref playerPosition);

                if (playerPosition.Row == _finishCoordinate.Row &&
                    playerPosition.Col == _finishCoordinate.Col)
                {
                    isWinner = true;
                    break;
                }
            } while (keyPressed.Key != ConsoleKey.Escape);

            Console.ForegroundColor = DefaultConsoleFontColor;
            PrintByCoordinate((sbyte) (_height + _marginTopSize + 1), _marginLeftSize,
                (isWinner ? MessageSuccess : MessageFail));
            Console.Write($"\n\n{_marginLeft}");
        }
    }

    static class GameMenu
    {
        private const byte TimingDelayPrintingMenu = 15;
        private const char TextureBorderType = '▓', TexturePointerType = '»';
        private static readonly string Pointer = "" + TexturePointerType + TexturePointerType;

        private const ConsoleColor MenuColor = ConsoleColor.White,
            PointerColor = ConsoleColor.White;

        private static readonly ConsoleColor DefaultConsoleFontColor = Console.ForegroundColor;

        private static readonly string[] MenuItems =
            {"Play", "Show Solution", "Visualization with DFS", "Visualization with BFS", "Exit"};

        private static readonly sbyte MaxMenuItemWidth = (sbyte) MenuItems.Max(item => item.Length);

        private const byte LeftPaddingSize = 6, RightPaddingSize = 6, PointerLeftMarginSize = 2;

        private static readonly string LeftPadding = new string(' ', LeftPaddingSize),
            RightPadding = new string(' ', RightPaddingSize);

        private static readonly sbyte FullHeight = (sbyte) (4 * MenuItems.Length),
            FullWidth = (sbyte) (1 + LeftPaddingSize + MaxMenuItemWidth + RightPaddingSize + 1);

        private static readonly string BorderInMenuList = new string(TextureBorderType, FullWidth);

        private static readonly sbyte MarginLeftSize = (sbyte) (Console.WindowWidth / 2 - FullWidth / 2 - 1),
            MarginTopSize = (sbyte) (Console.WindowHeight / 2 - FullHeight / 2 - 1);

        private static readonly string MarginLeft = new string(' ', MarginLeftSize),
            MarginTop = new string('\n', MarginTopSize);

        private static void PrintMenu()
        {
            Console.Clear();

            Console.Write(MarginTop);
            Console.ForegroundColor = MenuColor;
            Console.Write(MarginLeft + BorderInMenuList + '\n');
            Console.ForegroundColor = DefaultConsoleFontColor;
            foreach (var menuItem in MenuItems)
            {
                var currentRightPadding = new string(' ',
                    FullWidth - 2 - menuItem.Length - LeftPaddingSize - RightPaddingSize);
                var paddingRow = new string(' ', FullWidth - 2);
                Console.ForegroundColor = MenuColor;
                Console.Write(MarginLeft + TextureBorderType + paddingRow + TextureBorderType + "\n");
                Console.Write(MarginLeft + TextureBorderType + LeftPadding);
                Thread.Sleep(TimingDelayPrintingMenu);

                Console.ForegroundColor = DefaultConsoleFontColor;
                Console.Write(menuItem.ToUpper() + currentRightPadding + RightPadding);
                Thread.Sleep(TimingDelayPrintingMenu);

                Console.ForegroundColor = MenuColor;
                Console.Write(TextureBorderType + "\n");
                Console.Write(MarginLeft + TextureBorderType + paddingRow + TextureBorderType + "\n");
                Console.WriteLine(MarginLeft + BorderInMenuList);
                Thread.Sleep(TimingDelayPrintingMenu);
            }
        }

        private static void PrintByCoordinate(sbyte y, sbyte x, string content)
        {
            Console.SetCursorPosition(x, y);
            Console.Write(content);
        }

        private static void ComputeKeyPressed(ref ConsoleKeyInfo keyPressed, ref byte selectedItem)
        {
            switch (keyPressed.Key)
            {
                case ConsoleKey.UpArrow:
                {
                    if (selectedItem == 0)
                        selectedItem = (byte) (MenuItems.Length - 1);
                    else
                        --selectedItem;
                    break;
                }
                case ConsoleKey.DownArrow:
                {
                    ++selectedItem;
                    break;
                }
                default: return;
            }

            selectedItem = (byte) (selectedItem % MenuItems.Length);
        }

        private static void MoveMenuPointer(ref byte previous, ref byte current)
        {
            PrintByCoordinate((sbyte) (MarginTopSize + 2 + previous * 4),
                (sbyte) (MarginLeftSize + 1 + PointerLeftMarginSize),
                "  ");

            PrintByCoordinate((sbyte) (MarginTopSize + 2 + current * 4),
                (sbyte) (MarginLeftSize + 1 + PointerLeftMarginSize),
                Pointer);
        }

        private static byte MoveThroughMenu()
        {
            ConsoleKeyInfo keyPressed;
            Console.ForegroundColor = PointerColor;
            PrintByCoordinate((sbyte) (MarginTopSize + 2), (sbyte) (MarginLeftSize + 1 + PointerLeftMarginSize),
                Pointer);
            var selectedItem = (byte) 0;
            do
            {
                var previousItem = selectedItem;
                keyPressed = Console.ReadKey(true);
                if (keyPressed.Key == ConsoleKey.Enter)
                    break;
                ComputeKeyPressed(ref keyPressed, ref selectedItem);
                if (selectedItem != previousItem)
                {
                    MoveMenuPointer(ref previousItem, ref selectedItem);
                }
            } while (keyPressed.Key != ConsoleKey.Enter);

            return selectedItem;
        }

        public static void Launch()
        {
            while (true)
            {
                Console.CursorVisible = false;
                Console.Clear();
                Console.WriteLine("PRESS ANY KEY TO LAUNCH");
                Console.CursorVisible = false;
                Console.ReadKey(true);
                PrintMenu();
                Console.CursorVisible = false;
                var response = MoveThroughMenu();
                Console.Clear();
                var path = "labirint.txt";
                Console.CursorVisible = false;

                Labyrinth.LoadLabyrinth(ref path);
                switch (response)
                {
                    case 0:
                    {
                        Labyrinth.Play();
                        break;
                    }
                    case 1:
                    {
                        Labyrinth.PassByComputerBFS();
                        break;
                    }
                    case 2:
                    {
                        Labyrinth.VisualizePassingByComputerWithDFS();
                        break;
                    }
                    case 3:
                    {
                        Labyrinth.VisualizePassingByComputerWithBFS();
                        break;
                    }
                    case 4: return;
                }
                
                Console.ReadKey(true);
            }
        }
    }
}