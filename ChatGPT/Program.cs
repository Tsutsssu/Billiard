using System;
using System.Collections.Generic;
using System.Diagnostics;

class Program
{
    const int N = 11;
    static readonly int targetSum = N*(N-1) +1;
    static readonly int sup = (targetSum-1)/2 +1;

    static void Main()
    {
        var sw = Stopwatch.StartNew();
        int[] result = new int[N];
        result[0] = 1;

        var candidate = new List<int[]>();
        var indexMemo = new List<int>();

        int[] tmp = new int[sup-1];
        for (int i = 0; i < sup-1; i++) tmp[i] = i+2;
        candidate.Add((int[])tmp.Clone());
        indexMemo.Add(0);

        int depth = 1;
        int tmpIndex = 0;

        Console.WriteLine($"{N} 角形");

        while (result[0] != 0)
        {
            result[depth] = tmp[tmpIndex];
            int partialSum = 0;
            bool valid = true;
            var tmpList = new List<int>(tmp);

            for (int j = depth; j >= 0; j--)
            {
                partialSum += result[j];

                if (!tmpList.Remove(Math.Min(partialSum, targetSum-partialSum)))
                {
                    valid = false;
                    break;
                }
            }

            if (!valid)
            {
                // バックトラック
                result[depth] = 0;
                while ((depth >= 1 && candidate[depth-1].Length <= tmpIndex+1)||(depth == N/2 && candidate[depth-1][0] == 2))
                {
                    depth--;
                    tmpIndex = indexMemo[depth];
                    indexMemo.RemoveAt(depth);
                    candidate.RemoveAt(depth);
                    result[depth] = 0;
                }
                if (depth == 0) break;
                tmp = (int[])candidate[depth-1].Clone();
                tmpIndex++;
                continue;
            }

            if (depth >= N-2)
            {
                // 解を発見
                result[N-1] = targetSum - partialSum;
                Console.WriteLine(string.Join(",", result));

                // バックトラック
                result[depth] = 0;
                while ((depth >= 1 && candidate[depth-1].Length <= tmpIndex+1)||(depth == N/2 && candidate[depth-1][0] == 2))
                {
                    depth--;
                    tmpIndex = indexMemo[depth];
                    indexMemo.RemoveAt(depth);
                    candidate.RemoveAt(depth);
                    result[depth] = 0;
                }
                if (depth == 0) break;
                tmp = (int[])candidate[depth-1].Clone();
                tmpIndex++;
            }
            else
            {
                // 次の深さへ進む
                tmp = tmpList.ToArray();
                candidate.Add((int[])tmp.Clone());
                indexMemo.Add(tmpIndex);
                tmpIndex = 0;
                depth++;
            }
        }

        sw.Stop();
        Console.WriteLine($"C#      実行時間: {sw.Elapsed.TotalSeconds:F4}");
    }
}
