ls -l | awk '{if ($5>104857600) print $5, $9}'
