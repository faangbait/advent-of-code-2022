# Day 6: Part 2

Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

- `mjqjpqmgbljsphdztnvjfqwrcgsmlb`: first marker after character 19
- `bvwbjplbgvbhsrlpgdmjqwftvncz`: first marker after character 23
- `nppdvjthqldpwncqszvftbrmjlhg`: first marker after character 23
- `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`: first marker after character 29
- `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`: first marker after character 26

How many characters need to be processed before the first start-of-message marker is detected?

## Analysis
- I guess I did this right the first time, because all we need to do is change buf[-4:] to buf[-14:]
- This still has a linear time complexity, though it is O(14 * n) instead of O(4 * n). Iterating through the input string is O(n), slicing is O(1), and doing a fixed-length count of elements is O(14).
