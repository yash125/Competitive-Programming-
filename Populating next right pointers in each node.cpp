class Solution {
public:
    Node* connect(Node* root) {
        if(!root)
            return NULL;
        
        queue<Node*>q;
        q.push(root);
        Node* x=NULL;
        while(q.size())
        {
            int size=q.size();
            int c=0;
            for(int i=0;i<size;i++)
            {
                auto a = q.front();
                q.pop();
                if(!x)
                    x=a;
                else
                {
                    x->next = a;
                    x = x->next;
                }
                if(a->left)
                    q.push(a->left);
                if(a->right)
                    q.push(a->right);
                if(c==size-1){
                    a->next=NULL;
                    x=NULL;
                }
                c++;
                    
            }
        }
        return root;
        
    }
};