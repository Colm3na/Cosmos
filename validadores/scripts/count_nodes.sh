#! /bin/bash
echo localhost > nodes.log
while [ -s nodes.log ]
do
          # get first node from TODO list and store a copy
          node=$(head -n1 nodes.log)
          echo "Now accessing node $node."
          if grep -Fxq "$node" nl.log
            then
              # code if found
              echo "Node already queried"
              sed -i '1d' nodes.log
            else
              # code if not found
              echo $node >> nl.log
              sed -i '1d' nodes.log
              echo "Curling $node..."
              curl -m 2 -s http://$node:26657/net_info|grep -E '\"id\":|\"listen_addr":'|sed 's/"id": "//g'|sed 's/",//g'|sed 's/"listen_addr": "/@/g'|sed 's/^[ \t]*//g'|sed ':a;N;$!ba;s/\n@/@/g'|sed 's/.*@//'|sed 's/:.*//' >> nodes.log
              echo "Finished curling $node"
          fi
done
echo "###############################################"
echo "###############################################"
echo "###############################################"
echo "Finished & Found $(wc -l nl.log) nodes"
echo "###############################################"
echo "###############################################"
echo "###############################################"
