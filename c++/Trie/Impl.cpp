#include <map>
#include <string>
using namespace std;
/**
 * All of the operations are done in O(m) time where m is the size of the string.
    This is beneficial over normal BSTs because it doesn't require log(n) time where n is the number of words in the database and can scale.
    It's beeficial over hashmaps which does things in a O(1) timescale because there's no way to look for prefixes with hashmaps

    It's commonly implemented is google search and other search algorithms. (Remember the contains function within ProveIt? That's
                                                                            a less efficient version with it's O(m*n logn)) time complexity.
 */

class TrieNode
{
public:
    map<char, TrieNode *> children;
    bool is_word = false;

    TrieNode() {} // default ctor
};

class PrefixTree
{
public:
    PrefixTree()
    {
        root = new TrieNode();
    }

    void insert(string word)
    {
        TrieNode *curr = root;

        for (char c : word)
        {
            map<char, TrieNode *>::iterator it = curr->children.find(c); // just to see the type. Check docs for it's API
            if (it == curr->children.end())
            { // so you don't make a new TrieNode everytime
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->is_word = true;
    }

    bool search(string word)
    {
        TrieNode *curr = root;

        for (auto c : word)
        {
            if (curr->children.find(c) == curr->children.end())
            {
                return false;
            }
            curr = curr->children[c];
        }

        return curr->is_word;
    }

    bool startsWith(string prefix)
    {
        TrieNode *curr = root;

        for (auto c : prefix)
        {
            if (curr->children.find(c) == curr->children.end())
            {
                return false;
            }
            curr = curr->children[c];
        }

        return true;
    }

private:
    TrieNode *root;
};
