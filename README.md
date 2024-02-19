# loop_benchmark_python

## Results

<table>
    <tr>
        <th>Bubblesort</th>
        <th>Bubblesort with C</th>
        <th>Sum</th>
        <th>Sum with Numpy></th>
        <th>Sum with C</th>
    </tr>
    <tr>
        <td>926.816us</td>
        <td>29.635us</td>
        <td>4.482us</td>
        <td>3.581us</td>
        <td>0.927us</td>
    </tr>
</table>

## Run Benchmark
Compile the custom library in C.
```
cc -fPIC -shared -o lib.so lib.c
```

Run the python program
```
python3 main.py
```

