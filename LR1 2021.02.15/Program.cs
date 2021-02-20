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
            Console.ReadKey(true);
            var filePath = "labirint.txt";
            var game = new Labirint(ref filePath);
            //game.Play();
            //game.PassByComputerBFS();
            game.PassByComputerDFS();
            Console.ReadKey(true);
        }
    }

    class Labirint
    {
        private struct Position
        {
            public sbyte Row, Col;
        }

        private static readonly sbyte[,] Directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        private static sbyte _marginLeftSize, _marginTopSize;
        private static string _marginLeft, _marginTop;

        private const string Texture = "██", FreeSpace = "  ";
        private static readonly ConsoleColor DefaultConsoleFontColor = Console.ForegroundColor;

        private static readonly ConsoleColor ColorPlayer = ConsoleColor.DarkGreen,
            ColorAutoPassHead = ConsoleColor.DarkRed,
            ColorAutoPassBody = ConsoleColor.Green;

        private const string MessageSuccess = "PASSED SUCCESSFULLY",
            MessageFail = "FAILED TO PASS",
            MessageFinal = "PRESS ANY KEY";

        private const byte TimingDelayBFS = 60, TimingDelayDFSIn = 40, TimingDelayDFSOut = 7;

        private readonly byte _width, _height;
        private readonly List<List<bool>> _field = new List<List<bool>>();

        private readonly Position _startCoordinate = new Position {Row = -1, Col = -1},
            _finishCoordinate = new Position {Row = -1, Col = -1};

        public Labirint(ref string fileName)
        {
            Console.CursorVisible = false;
            var lines = File.ReadAllLines(fileName);
            this._height = Convert.ToByte(lines[0].Split(' ')[0]);
            this._width = Convert.ToByte(lines[0].Split(' ')[1]);
            for (sbyte counter = 1; counter < this._height + 1; ++counter)
            {
                var tempRowList = lines[counter].Select(state => state != '█').ToList();
                this._field.Add(tempRowList);
            }

            this._startCoordinate.Row += sbyte.Parse(lines[^2].Split(' ')[0]);
            this._startCoordinate.Col += sbyte.Parse(lines[^2].Split(' ')[1]);
            this._finishCoordinate.Row += sbyte.Parse(lines[^1].Split(' ')[0]);
            this._finishCoordinate.Col += sbyte.Parse(lines[^1].Split(' ')[1]);

            _marginLeftSize = (sbyte) (Console.WindowWidth / 2 - this._width - 1);
            _marginTopSize = (sbyte) (Console.WindowHeight / 2 - this._height / 2 - 1);
            _marginLeft = new string(' ', _marginLeftSize);
            _marginTop = new string('\n', _marginTopSize);
        }

        private void PrintField()
        {
            Console.OutputEncoding = Encoding.UTF8;

            Console.Write(_marginTop);
            Console.ForegroundColor = DefaultConsoleFontColor;
            foreach (var row in this._field)
            {
                Console.Write(_marginLeft);
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

        private void SearchInLabirint(ref bool foundPath, ref int[,] visitedPositions)
        {
            var visitedCells = new Queue<Position>();

            visitedCells.Enqueue(this._startCoordinate);

            while (visitedCells.Count > 0 && !foundPath)
            {
                var currentPosition = visitedCells.Dequeue();
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (SByte) (currentPosition.Col + Directions[counter, 0]);
                    var y = (SByte) (currentPosition.Row + Directions[counter, 1]);

                    if (x >= 0 && x < this._width && y >= 0 && y < this._height && visitedPositions[y, x] == 0 &&
                        !(x == this._startCoordinate.Col && y == this._startCoordinate.Row))
                    {
                        visitedPositions[y, x] = visitedPositions[currentPosition.Row, currentPosition.Col] + 1;
                        visitedCells.Enqueue(new Position {Row = y, Col = x});
                    }

                    if (y == this._finishCoordinate.Row && x == this._finishCoordinate.Col)
                    {
                        foundPath = true;
                        break;
                    }
                }
            }
        }

        private Position[] GetPath(ref int[,] visitedPositions)
        {
            var path = new Position[visitedPositions[_finishCoordinate.Row, _finishCoordinate.Col] + 1];
            int pathIndex = 0;
            path[pathIndex] = _finishCoordinate;

            while (!(path[pathIndex].Row == this._startCoordinate.Row &&
                     path[pathIndex].Col == this._startCoordinate.Col))
            {
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (SByte) (path[pathIndex].Col + Directions[counter, 0]);
                    var y = (SByte) (path[pathIndex].Row + Directions[counter, 1]);

                    if (x >= 0 && x < this._width && y >= 0 && y < this._height && visitedPositions[y, x] != -1 &&
                        visitedPositions[y, x] == visitedPositions[path[pathIndex].Row, path[pathIndex].Col] - 1)
                    {
                        path[++pathIndex] = (new Position {Row = y, Col = x});
                        break;
                    }
                }
            }

            return path;
        }

        private void ShowPassage(ref Position[] path)
        {
            this.PrintField();
            var previousCoordinate = this._startCoordinate;
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

        public void PassByComputerBFS()
        {
            var visitedPositions = new int[this._height, this._width];
            for (sbyte row = 0; row < this._height; ++row)
            for (sbyte col = 0; col < this._width; ++col)
                visitedPositions[row, col] = (_field[row][col] ? 0 : -1);

            visitedPositions[this._startCoordinate.Row, this._startCoordinate.Col] = 0;

            var foundPath = false;

            this.SearchInLabirint(ref foundPath, ref visitedPositions);

            if (foundPath)
            {
                var path = this.GetPath(ref visitedPositions).Reverse().ToArray();
                this.ShowPassage(ref path);
            }
            else
            {
                this.PrintField();
            }

            PrintByCoordinate((sbyte) (this._height + _marginTopSize + 1), _marginLeftSize,
                (foundPath ? MessageSuccess : MessageFail));
            Console.Write($"\n\n{_marginLeft}" + MessageFinal);
        }

        private void DFS(Position currentPosition, ref bool[,] visitedPositions, ref bool foundPath)
        {
            visitedPositions[currentPosition.Row, currentPosition.Col] = true;
            if (currentPosition.Row == this._finishCoordinate.Row && currentPosition.Col == this._finishCoordinate.Col)
            {
                foundPath = true;
                return;
            }

            for (sbyte counter = 0; counter < 4; ++counter)
            {
                var x = (sbyte) (currentPosition.Col + Directions[counter, 0]);
                var y = (sbyte) (currentPosition.Row + Directions[counter, 1]);

                if (x >= 0 && x < this._width && y >= 0 && y < this._height && this._field[y][x] == true &&
                    visitedPositions[y, x] == false)
                {
                    PrintByCoordinate((sbyte) (y + _marginTopSize), (sbyte) (x * 2 + _marginLeftSize), Texture);
                    Thread.Sleep(TimingDelayDFSIn);
                    this.DFS(new Position {Row = y, Col = x}, ref visitedPositions, ref foundPath);
                    Thread.Sleep(TimingDelayDFSOut);
                    PrintByCoordinate((sbyte) (y + _marginTopSize), (sbyte) (x * 2 + _marginLeftSize), FreeSpace);
                }
            }
        }

        public void PassByComputerDFS()
        {
            this.PrintField();
            
            var foundPath = false;
            var visitedPositions = new bool [this._height, this._width];
            for (sbyte row = 0; row < this._height; ++row)
            for (sbyte col = 0; col < this._width; ++col)
                visitedPositions[row, col] = !this._field[row][col];
            
            Console.ForegroundColor = ColorAutoPassBody;
            PrintByCoordinate((sbyte)(_startCoordinate.Row + _marginTopSize), (sbyte)(_startCoordinate.Col * 2 + _marginLeftSize), Texture);
            this.DFS(_startCoordinate, ref visitedPositions, ref foundPath);

            Console.ForegroundColor = DefaultConsoleFontColor;
            PrintByCoordinate((sbyte) (this._height + _marginTopSize + 1), _marginLeftSize,
                (foundPath ? MessageSuccess : MessageFail));
            Console.Write($"\n\n{_marginLeft}" + MessageFinal);
        }

        private void MovePlayer(ref Position previous, ref Position current)
        {
            PrintByCoordinate((sbyte) (previous.Row + _marginTopSize), (sbyte) (previous.Col * 2 + _marginLeftSize),
                FreeSpace);
            PrintByCoordinate((sbyte) (current.Row + _marginTopSize), (sbyte) (current.Col * 2 + _marginLeftSize),
                Texture);
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
            var isWinner = false;
            var playerPosition = this._startCoordinate;
            ConsoleKeyInfo keyPressed;

            this.PrintField();

            Console.ForegroundColor = ColorPlayer;
            PrintByCoordinate((sbyte) (playerPosition.Row + _marginTopSize),
                (sbyte) (playerPosition.Col * 2 + _marginLeftSize), Texture);
            do
            {
                keyPressed = Console.ReadKey(true);
                var previousPosition = playerPosition;

                this.ComputeKeyPressed(ref keyPressed, ref playerPosition);

                if (previousPosition.Col != playerPosition.Col || previousPosition.Row != playerPosition.Col)
                    MovePlayer(ref previousPosition, ref playerPosition);

                if (playerPosition.Row == this._finishCoordinate.Row &&
                    playerPosition.Col == this._finishCoordinate.Col)
                {
                    isWinner = true;
                    break;
                }
            } while (keyPressed.Key != ConsoleKey.Escape);

            Console.ForegroundColor = DefaultConsoleFontColor;
            PrintByCoordinate((sbyte) (this._height + _marginTopSize + 1), _marginLeftSize,
                (isWinner == true ? MessageSuccess : MessageFail));
            Console.Write($"\n\n{_marginLeft}" + MessageFinal);
        }
    }
}