# Command Line Interface

Command line options for adc

```bash
python -m adc [OPTIONS] input
```

## Options

| Option                | Type | Description                                       | Default    | Choices       |
|-----------------------|------|---------------------------------------------------|------------|---------------|
| `input`               | str  | Path to input (file or folder)                    | *required* | -             |
| `--output`            | str  | Path to output destination                        | *required* | -             |
| `--min_dist`          | int  | Maximum distance between two waypoints            | 25         | -             |
| `--extract_waypoints` | bool | Extract starting points of each track as waypoint | True       | [True, False] |
| `--elevation`         | bool | Include elevation data in waypoints               | True       | [True, False] |


## Examples


### 1. Basic usage

```bash
python -m adc input
```

### 2. With verbose logging

```bash
python -m adc -v input
python -m adc --verbose input
```

### 3. With quiet mode

```bash
python -m adc -q input
python -m adc --quiet input
```

### 4. With min_dist parameter

```bash
python -m adc --min_dist 25 input
```

### 5. With extract_waypoints parameter

```bash
python -m adc --extract_waypoints True input
```

### 6. With elevation parameter

```bash
python -m adc --elevation True input
```