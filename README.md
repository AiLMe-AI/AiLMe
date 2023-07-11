## AiLMe

[AiLMe](https://ailme.ai) is a multilingual large language model trained by AiLMe AI Lab. It can produce stories and articles, and it can also give you helpful answers when you ask questions. It's still in the beginning phase, but its ultimate goal is to make a super smart AI that can completely liberate humanity from various arduous tasks.

This project is an implementation of calling AiLMe API.


## Usage

The script accepts either a JSON string or a JSON file as an input, and supports both stream and non-stream outputs.

Before using the script, you need to get your auth-key and replace <your-auth-key> in the script with your actual key.

### Example 1: Command Line JSON Argument

```bash
python examples/ailme_api.py '{"messages": [{"content": "1+1=？", "role": "user"}]}'
```
In this example, a JSON string is passed as an argument. The script sends a request to the AILME API and prints the response.


### Example 2: JSON File Input

```json
{
  "messages": [
    {"content": "Hello, AI!", "role": "user"}
  ]
}
```
You can pass this file to the script:

```bash
python examples/ailme_api.py input.json
```
The script reads the file, sends a request to the AILME API for each line in the file, and prints the responses.

### Example 3: Stream Mode
The --stream flag enables stream mode, in which the script keeps the connection open and prints each response as it arrives. To use this mode, add the --stream flag:
```bash
python examples/ailme_api.py '{"messages": [{"content": "Hello, AI!", "role": "user"}]}' --stream
```
In this example, the script sends a request to the AILME API and prints each response as it arrives. If the response is delayed, the script will wait rather than terminating.

### Further Help

For further details, refer to the AILME API documentation, or use the -h or --help flag with the script:

```bash
python examples/ailme_api.py --help
```

## Citations

```bibtex
@article{2023ailme,
    title   = {AiLMe: a multilingual large language model},
    author  = {Xu Zhang and David D. Cox},
    howpublished = {\url{https://github.com/AiLMe-AI/AiLMe}},
    year    = {2023}
}
```
