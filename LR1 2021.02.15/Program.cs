using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;

namespace LR1_2021._02._15
{
    class Program
    {
        static void Main()
        {
            var filePath = "labirint.txt";
            var test = new Labirint(ref filePath);

            test.PassByComputer();
            Console.Read();
        }
    }

    class Labirint
    {
        private struct Position
        {
            public sbyte Row, Col;
        }

        private static readonly sbyte[,] Directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        private const byte MarginLeftSize = 4, MarginTopSize = 5;

        private static readonly string MarginLeft = new string(' ', MarginLeftSize),
            MarginTop = new string('\n', MarginTopSize);

        private const string Texture = "██", FreeSpace = "  ";
        private static readonly ConsoleColor DefaultConsoleFontColor = Console.ForegroundColor;

        private static readonly ConsoleColor ColorPlayer = ConsoleColor.DarkGreen,
            ColorAutoPassHead = ConsoleColor.DarkRed,
            ColorAutoPassBody = ConsoleColor.Green;

        private const string MessageSuccess = "PASSED SUCCESSFULLY", MessageFail = "FAILED TO PASS";
        private const ushort TimingDelay = 60;

        private readonly byte _width, _height;
        private readonly List<List<bool>> _field = new List<List<bool>>();

        private readonly Position _startCoordinate = new Position {Row = -1, Col = -1},
            _finishCoordinate = new Position {Row = -1, Col = -1};

        private void SearchInLabirint(ref bool foundPath, ref Queue<Position> bfs, ref int[,] visitedPositions)
        {
            bfs.Enqueue(this._startCoordinate);

            while (bfs.Count > 0 && !foundPath)
            {
                var currentPosition = bfs.Dequeue();
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (SByte) (currentPosition.Col + Directions[counter, 0]);
                    var y = (SByte) (currentPosition.Row + Directions[counter, 1]);

                    if (x >= 0 && x < this._width && y >= 0 && y < this._height && visitedPositions[y, x] == 0 &&
                        !(x == this._startCoordinate.Col && y == this._startCoordinate.Row))
                    {
                        visitedPositions[y, x] = visitedPositions[currentPosition.Row, currentPosition.Col] + 1;
                        bfs.Enqueue(new Position {Row = y, Col = x});
                    }

                    if (y == this._finishCoordinate.Row && x == this._finishCoordinate.Col)
                    {
                        foundPath = true;
                        break;
                    }
                }
            }
        }

        private List<Position> GetPath(ref int[,] visitedPositions)
        {
            var path = new List<Position> {this._finishCoordinate};

            while (!(path[^1].Row == this._startCoordinate.Row && path[^1].Col == this._startCoordinate.Col))
            {
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (SByte) (path[^1].Col + Directions[counter, 0]);
                    var y = (SByte) (path[^1].Row + Directions[counter, 1]);

                    if (x >= 0 && x < this._width && y >= 0 && y < this._height && visitedPositions[y, x] != -1 &&
                        visitedPositions[y, x] == visitedPositions[path[^1].Row, path[^1].Col] - 1)
                    {
                        path.Add(new Position {Row = y, Col = x});
                        break;
                    }
                }
            }

            return path;
        }

        private void PrintField()
        {
            Console.OutputEncoding = Encoding.UTF8;

            Console.Write(MarginTop);
            foreach (var row in this._field)
            {
                Console.Write(MarginLeft);
                foreach (var state in row) Console.Write(state ? "  " : Texture);
                Console.Write('\n');
            }

            Console.Write('\n');
        }

        private static void PrintByCoordinate(sbyte y, sbyte x, string info)
        {
            Console.SetCursorPosition(x, y);
            Console.Write(info);
        }
        
        private void ShowPassage(ref List<Position> path)
        {
            this.PrintField();
            var previousCoordinate = this._startCoordinate;
            foreach (var currentCoordinate in path)
            {
                Console.ForegroundColor = ColorAutoPassBody;
                Console.SetCursorPosition(previousCoordinate.Col * 2 + MarginLeftSize,
                    previousCoordinate.Row + MarginTopSize);
                Console.Write(Texture);

                previousCoordinate = currentCoordinate;
                Console.ForegroundColor = ColorAutoPassHead;

                Console.SetCursorPosition(currentCoordinate.Col * 2 + MarginLeftSize,
                    currentCoordinate.Row + MarginTopSize);
                Console.Write(Texture);

                Thread.Sleep(TimingDelay);
            }

            Console.ForegroundColor = DefaultConsoleFontColor;
            Console.SetCursorPosition(MarginLeftSize, this._height + MarginTopSize);
            Console.WriteLine($"\n{MarginLeft}{MessageSuccess}");
        }

        private void MovePlayer(ref Position previous, ref Position current)
        {
            PrintByCoordinate((sbyte)(previous.Row + MarginTopSize), (sbyte)(previous.Col * 2 + MarginLeftSize), FreeSpace);
            PrintByCoordinate((sbyte)(current.Row + MarginTopSize), (sbyte)(current.Col * 2 + MarginLeftSize), Texture);
        }

        public Labirint(ref string fileName)
        {
            Console.CursorVisible = false;
            var lines = File.ReadAllLines(fileName);
            this._height = Convert.ToByte(lines[0].Split(' ')[0]);
            this._width = Convert.ToByte(lines[0].Split(' ')[1]);
            for (sbyte counter = 1; counter < this._height + 1; ++counter)
            {
                var tempRowList = new List<bool>();
                foreach (var state in lines[counter].Split(' ').ToArray())
                    tempRowList.Add(Convert.ToBoolean(Convert.ToSByte(state.Trim())));
                this._field.Add(tempRowList);
            }

            this._startCoordinate.Row += sbyte.Parse(lines[^2].Split(' ')[0]);
            this._startCoordinate.Col += sbyte.Parse(lines[^2].Split(' ')[1]);
            this._finishCoordinate.Row += sbyte.Parse(lines[^1].Split(' ')[0]);
            this._finishCoordinate.Col += sbyte.Parse(lines[^1].Split(' ')[1]);
        }

        public void PassByComputer()
        {
            var visitedPositions = new int[this._height, this._width];
            for (sbyte row = 0; row < this._height; ++row)
            for (sbyte col = 0; col < this._width; ++col)
                visitedPositions[row, col] = (_field[row][col] ? 0 : -1);

            visitedPositions[this._startCoordinate.Row, this._startCoordinate.Col] = 0;

            var bfs = new Queue<Position>();
            var foundPath = false;

            this.SearchInLabirint(ref foundPath, ref bfs, ref visitedPositions);

            if (foundPath)
            {
                var path = this.GetPath(ref visitedPositions);
                path.Reverse();
                this.ShowPassage(ref path);
            }
            else
            {
                this.PrintField();
                Console.WriteLine(MessageFail);
            }
        }

        private void ComputeKeyPressed(ref ConsoleKeyInfo keyPressed, ref Position player)
        {
            switch (keyPressed.Key)
            {
                case ConsoleKey.UpArrow:
                {
                    if (player.Row - 1 >= 0 && this._field[player.Row - 1][player.Col])
                        --player.Row;
                    break;
                }
                case ConsoleKey.DownArrow:
                {
                    if (player.Row + 1 < this._height && this._field[player.Row + 1][player.Col])
                        ++player.Row;
                    break;
                }
                case ConsoleKey.LeftArrow:
                {
                    if (player.Col - 1 >= 0 && this._field[player.Row][player.Col - 1])
                        --player.Col;
                    break;
                }
                case ConsoleKey.RightArrow:
                {
                    if (player.Col + 1 < this._height && this._field[player.Row][player.Col + 1])
                        ++player.Col;
                    break;
                }
            }
        }
        
        public void Play()
        {
            this.PrintField();
            var player = this._startCoordinate;
            ConsoleKeyInfo keyPressed;
            Console.SetCursorPosition(this._startCoordinate.Col * 2 + MarginLeftSize,
                this._startCoordinate.Row + MarginTopSize);
            Console.ForegroundColor = ColorPlayer;
            Console.Write(Texture);
            do
            {
                keyPressed = Console.ReadKey(true);
                var previousPosition = player;
                
                this.ComputeKeyPressed(ref keyPressed, ref player);
                
                if (previousPosition.Col != player.Col || previousPosition.Row != player.Col)
                    MovePlayer(ref previousPosition, ref player);
                
            } while (keyPressed.Key != ConsoleKey.Escape || keyPressed.Key != ConsoleKey.Backspace);

            Console.ForegroundColor = DefaultConsoleFontColor;
        }
    }
}